

BACKOFF_CONFIG = {
    "user-free": {
        "priority-low": {
            "cpu":      [[0, 40, 60, 70], 
                        [0, 1, 3, 5]],
            "memory":   [[0, 50, 70, 80], 
                        [0, 1, 3, 5]],
            "latency":  [[0, 0.2, 0.3, 0.5], 
                        [0, 1, 3, 5]],
        },
        "priority-medium": {
            "cpu":      [[0, 40, 60, 70], 
                        [0, 1, 2, 4]],
            "memory":   [[0, 50, 70, 80], 
                        [0, 1, 2, 4]],
            "latency":  [[0, 0.2, 0.3, 0.5], 
                        [0, 1, 2, 4]],
        },
        "priority-high": {
            "cpu":      [[0, 40, 60, 70], 
                        [0, 0, 1, 2]],
            "memory":   [[0, 50, 70, 80], 
                        [0, 0, 1, 2]],
            "latency":  [[0, 0.2, 0.3, 0.5], 
                        [0, 0, 1, 2]],
        }
    },
    "user-paid": {
        "priority-low": {
            "cpu":      [[0, 40, 60, 70], 
                        [0, 1, 2, 4]],
            "memory":   [[0, 50, 70, 80], 
                        [0, 1, 2, 4]],
            "latency":  [[0, 0.2, 0.3, 0.5], 
                        [0, 1, 2, 4]],
        },
        "priority-medium": {
            "cpu":      [[0, 40, 60, 70], 
                        [0, 0, 1, 2]],
            "memory":   [[0, 50, 70, 80], 
                        [0, 0, 1, 2]],
            "latency":  [[0, 0.2, 0.3, 0.5], 
                        [0, 0, 1, 2]],
        },
        "priority-high": {
            "cpu":      [[0, 40, 60, 70], 
                        [0, 0, 0, 1]],
            "memory":   [[0, 50, 70, 80], 
                        [0, 0, 0, 1]],
            "latency":  [[0, 0.2, 0.3, 0.5], 
                        [0, 0, 0, 1]],
        }
    }
}