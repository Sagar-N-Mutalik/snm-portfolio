from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Renders the Home / About Me page."""
    template_name = 'website/index.html'


class ProjectsView(TemplateView):
    """Renders the Projects showcase page."""
    template_name = 'website/projects.html'


class LeadershipView(TemplateView):
    """Renders the Leadership & Community page."""
    template_name = 'website/leadership.html'
