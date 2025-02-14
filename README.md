# Health-check

This repository contains a Python script to monitor the health and availability of multiple endpoints, which are defined in a YAML configuration file. The script checks the endpoints periodically every 15 seconds and reports their availability percentage based on their response status and latency.

### Packages Used
The following Python packages are required to run this script:

* requests: For making HTTP requests to the endpoints and checking their status.
* pyyaml: For parsing YAML configuration files.
* time: For time-related operations such as measuring response time.
* collections: For managing and storing endpoint stats.
* urllib: For URL parsing.

You can install the required packages using pip by running:

```
pip install requests pyyaml
```

### How to Run the Script
1. The script expects a YAML file containing the configuration for the endpoints you want to monitor.
   
   ```yaml
   # Sample YAML
   - headers:
       user-agent: fetch-synthetic-monitor
     method: GET
     name: fetch index page
     url: 'https://fetch.com/'
   - headers:
       user-agent: fetch-synthetic-monitor
     method: GET
     name: fetch careers page
     url: 'https://fetch.com/careers'
   - body: '{"foo":"bar"}'
     headers:
       content-type: application/json
       user-agent: fetch-synthetic-monitor
     method: POST
     name: fetch some fake post endpoint
     url: 'https://fetch.com/some/post/endpoint'
   - name: fetch rewards index page
     url: 'https://www.fetchrewards.com/'
   ```
2. Run the script:
   You can run the script by providing the path to your YAML file as a command-line argument.

   ```python
   python health_check.py /path/to/your/config.yaml
   ```
   The script will continue to run indefinitely, checking the health of the endpoints every 15 seconds and printing the availability percentage for 
   each domain. You can stop the script by pressing Ctrl+C.

   Example Output:
   
   ```
   fetch.com has 67% availability percentage
   www.fetchrewards.com has 100% availability percentage
   ```
3. Stop the script:
   To stop the monitoring process, simply press Ctrl+C in the terminal. The script will handle the interruption and exit.
   
