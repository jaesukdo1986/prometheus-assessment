from flask import Flask, Response
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
from elasticsearch import Elasticsearch
import os
import time
import threading

# Initialize Flask app
app = Flask(__name__)

# Initialize Prometheus metrics
documents_count = Gauge('elasticsearch_document_count', 'Number of documents in Elasticsearch index', ['index'])

# Initialize Elasticsearch client
es_host = os.environ.get('ELASTICSEARCH_HOST', 'localhost')
es_port = os.environ.get('ELASTICSEARCH_PORT', '9200')
es_index = os.environ.get('ELASTICSEARCH_INDEX', 'filebeat-*')
es = Elasticsearch([f'http://{es_host}:{es_port}'])

def update_document_count():
    """Query Elasticsearch and update the document count metric"""
    try:
        # Count documents in the index
        count = es.count(index=es_index)['count']
        # Update the gauge with the current count
        documents_count.labels(index=es_index).set(count)
        print(f"Updated document count for index {es_index}: {count}")
    except Exception as e:
        print(f"Error updating document count: {e}")

def background_updater():
    """Background thread to periodically update the document count"""
    while True:
        update_document_count()
        time.sleep(60)  # Update every minute

@app.route('/metrics')
def metrics():
    """Endpoint to expose metrics"""
    # Update the document count before serving metrics
    update_document_count()
    # Generate and return metrics
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/')
def home():
    """Root endpoint"""
    return "Elasticsearch Document Count Exporter. Visit /metrics for Prometheus metrics."

if __name__ == '__main__':
    # Start the background updater thread
    updater_thread = threading.Thread(target=background_updater, daemon=True)
    updater_thread.start()
    
    # Get port from environment or use default
    port = int(os.environ.get('PORT', 8000))
    # Start the server
    app.run(host='0.0.0.0', port=port)
