from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.http import HttpResponseRedirect
#from .forms import NameForm


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Black Bin Waste"]

    def get_data(self):
        """Return datasets to plot."""

        return [[20, 25, 21, 18, 14, 13, 13],]

line_chart = TemplateView.as_view(template_name='line_chart.html')
line_chart_json = LineChartJSONView.as_view()
