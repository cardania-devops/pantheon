class SignalReceiver:
    def __init__(self):
        # Initialization for any required attributes
        pass

    def receive_signal(self, signal):
        # Implement logic to handle received signals
        formatted_signal = f"Signal received: {signal}"
        self.process_signal(formatted_signal)
        return formatted_signal

    def process_signal(self, signal):
        # Placeholder for processing logic
        # Example: Log the signal or trigger another action
        print(f"Processing signal: {signal}")
        # Add more complex processing as needed
