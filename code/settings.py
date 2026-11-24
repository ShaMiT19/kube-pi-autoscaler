# Cluster settings shared by all components.
# Update these values to match your own cluster before running anything.

# Kubernetes node names, exactly as shown by `kubectl get nodes`.
# Index 0 is the master node, indices 1 and 2 are the worker nodes.
NODES = ["node0", "node1", "node2"]

# IP address of each node, in the same order as NODES.
# The master node runs the middleware and the global controller.
NODE_IPS = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
MASTER_IP = NODE_IPS[0]

# Ports
MIDDLEWARE_PORT = 6666
LOCAL_CONTROLLER_PORT = 6667

MIDDLEWARE_URL = f"http://{MASTER_IP}:{MIDDLEWARE_PORT}"
LOCAL_CONTROLLER_URLS = {
    node: f"http://{ip}:{LOCAL_CONTROLLER_PORT}/" for node, ip in zip(NODES, NODE_IPS)
}

# Controller tuning
REFERENCE_INPUT = 0.8      # target CPU utilisation (80%), shared by both controllers
PI_KP = -3.127             # PI controller proportional gain
PI_KI = 3.1406             # PI controller integral gain
LOCAL_SAMPLING_RATE = 5    # seconds between local controller decisions
MAX_PODS_LIMIT = 12        # upper bound for MAXPODS on a node
