#!/usr/bin/env python3

import sys
import time
import logging
import base64
import urllib3
import json
from docopt import docopt
import requests
from datetime import datetime

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('cluster_creation.log')
    ]
)
logger = logging.getLogger(__name__)


CONFIG = {
    'user' : 'admin',
    'password' : 'netapp1234',

}

def get_args():
	"""Function to get command line arguments.

	Defines arguments needed to run this program.

	:return: Dictionary with arguments
	:rtype: dict
	"""
	
	usage = """
        Usage:
        createCluster.py -s <STORAGE> -n <NODE_NAME> -p <PASSWORD>
        createCluster.py (-h | --help)
        createCluster.py --version

        Options:
        -s <STORAGE>              Management STORAGE address of the node
        -n <NODE_NAME>       Node name to assign
        -p <PASSWORD>        Admin password for the cluster
        -h --help            Show this screen
        --version            Show version
"""

	args = docopt(usage)
	return args	

def Headers():
    userpass = f'{CONFIG["user"]}:{CONFIG["password"]}'
    encoded_credentials = base64.b64encode(userpass.encode()).decode()
    return {"Authorization": f"Basic {encoded_credentials}"}

def createCluster():
    storage = ARGS["-s"]
    name = ARGS["-n"]
    passwd = ARGS["-p"]

    headers = Headers()

    url = f'https://{storage}/api/cluster/'
    data = {
            "name": name,
            "password": passwd,
            "single_node_cluster": True  # Set to False for multi-node clusters
        }
        
    logger.info(f"Creating cluster '{name}'...")
        
    try:
        response = requests.post(
            url, 
            headers=headers, 
            json=data,
            verify=False,
            timeout=30
        )
        
        if response.status_code in [200, 201, 202]:
            result = response.json()
            logger.info(f"Cluster creation initiated successfully: {result}")
            return result
        else:
            logger.error(f"Failed to create cluster. Status code: {response.status_code}")
            logger.error(f"Response: {response.text}")
            return None
                
    except Exception as e:
        logger.error(f"Error creating cluster: {str(e)}")
        return None

if __name__ == '__main__':

    ARGS = get_args()


    startTime = time.time()
    logger.info("Starting to create new cluster")

    result = createCluster()

    if not result:
        
        logger.error(f'No cluster created.')
        sys.exit(1)

    # Get job ID from result
    job_id = result.get("job", {}).get("uuid")
    
    if not job_id:
        logger.error("No job ID returned from cluster creation request.")
        sys.exit(1)

    endTime = time.time() - startTime
    logger.error(f"Execution time: {endTime:.6f} seconds")