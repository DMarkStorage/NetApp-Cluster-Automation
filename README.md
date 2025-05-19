
Automating NetApp Cluster Creation with Python
------------------------------------------------

*DevOps | Python | NetApp*


A Python script that automates the creation of NetApp clusters through the REST API, significantly reducing deployment time and eliminating manual configuration errors.


### 🛠️ What It Does





- **Simple Command-Line Interface**: Create clusters with just a few parameters
- **Secure Authentication**: Handles Basic Auth for API access
- **Comprehensive Logging**: Maintains detailed logs of all operations
- **Error Handling**: Robust error reporting for troubleshooting
- **Configurable Options**: Supports both single-node and multi-node clusters



## Requirements

- Python 3.6 or higher
- Network access to NetApp storage system
- Admin credentials for the NetApp system
- Required Python packages (see Installation section)

## Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/netapp-cluster-automation.git
cd netapp-cluster-automation
```

Install required dependencies:

```bash
pip install docopt requests urllib3
```

## Usage

Basic usage is as follows:

```bash
python createCluster.py -s <STORAGE_IP> -n <CLUSTER_NAME> -p <ADMIN_PASSWORD>
```

### Parameters

- `-s <STORAGE>`: Management IP address of the NetApp storage system
- `-n <NODE_NAME>`: Name to assign to the new cluster
- `-p <PASSWORD>`: Admin password for the cluster
- `-h --help`: Show help screen
- `--version`: Show version information

### Example

```bash
python createCluster.py -s storage.example.com -n new-cluster -p securePassword123
```

## How It Works

- The script authenticates to the NetApp system using Basic Auth
- It constructs a JSON payload with the cluster configuration
- The payload is sent to the NetApp REST API endpoint
- The script monitors the job status and reports the result
- All operations are logged both to console and log file

## Advanced Configuration

### Multi-Node Clusters

To create a multi-node cluster instead of a single-node cluster, modify the `single_node_cluster` parameter in the data dictionary:

```python
data = {
    "name": name,
    "password": passwd,
    "single_node_cluster": False  # Set to True for single-node clusters
}
```

### Customizing Credentials

Default credentials are stored in the CONFIG dictionary:

```python
CONFIG = {
    'user': 'admin',
    'password': 'netapp1234',
}
```

> For production use, consider modifying the script to retrieve credentials from environment variables or a secure credential store.

## Logging

The script logs all operations to both the console and a log file (`cluster_creation.log`). The log format includes timestamps, log levels, and detailed messages:

```
2025-05-19 14:30:25,642 - INFO - Starting to create new cluster
2025-05-19 14:30:27,154 - INFO - Creating cluster 'new-cluster'...
2025-05-19 14:30:28,879 - INFO - Cluster creation initiated successfully: {'job': {'uuid': '1234-5678-9abc-def0'}}
2025-05-19 14:30:28,881 - ERROR - Execution time: 3.239000 seconds
```

## Error Handling

The script implements comprehensive error handling to catch and report issues:

- API connection failures
- Authentication errors
- Invalid configuration parameters
- Timeouts during operation
- Job execution failures

### 🧪 Sample Output



```
{
  "job": {
    "uuid": "f25d3e50-xxxx-xxxx-xxxx-1d02099f06af"
  }
}
```

### Performance


The script logs the total execution time for cluster creation, aiding performance tracking.


### Security Tip



> Never hardcode sensitive credentials in production scripts. Use environment variables or a secrets manager.


### Suggested Improvements


* Job status polling
* Multi-node cluster support
* Dynamic retry logic for API failures


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
