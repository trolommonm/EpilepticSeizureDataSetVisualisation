import plotly.graph_objects as go
import plotly

def getGraph(cols, data, seizureOrNot):
	fig = go.Figure(data=go.Scatter(x=cols, y=data))
	if seizureOrNot == 1:
		fig.update_layout(title_text="Visualisation of EEG data for seizure")
	else:
		fig.update_layout(title_text="Visualisation of EEG data for non seizure")

	x = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')

	return x 

def getAnotherGraph(freq, data, seizureOrNot):
	fig = go.Figure(data=go.Scatter(x=freq, y=data))
	if seizureOrNot == 1:
		fig.update_layout(title_text="Visualisation of EEG data (in frequency domain) for seizure")
	else:
		fig.update_layout(title_text="Visualisation of EEG data (in frequency domain) for non seizure")

	x = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')

	return x 