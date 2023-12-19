class SignalGenerator:
    def __init__(self):
        # Initialization can be used for setting up thresholds or parameters
        pass

    def basic_signal_logic(self, interpreted_data):
        # Implement enhanced signal generation logic here
        signals = []
        for data in interpreted_data:
            score = data['score']
            if score > 0.7:
                signal = 'Extremely Bullish'
            elif 0.5 < score <= 0.7:
                signal = 'Very Bullish'
            elif 0.3 < score <= 0.5:
                signal = 'Slightly Bullish'
            elif -0.3 <= score <= 0.3:
                signal = 'Neutral'
            elif -0.5 <= score < -0.3:
                signal = 'Slightly Bearish'
            elif -0.7 <= score < -0.5:
                signal = 'Very Bearish'
            else:
                signal = 'Extremely Bearish'
            signals.append(signal)
        return signals
