from django_distill import distill_path
from .views import HomeView, ProjectsView, LeadershipView

def get_none():
    """Returns None as there are no dynamic URL parameters for these pages."""
    return None

urlpatterns = [
    distill_path('', HomeView.as_view(), name='home', distill_func=get_none),
    distill_path('projects/', ProjectsView.as_view(), name='projects', distill_func=get_none),
    distill_path('leadership/', LeadershipView.as_view(), name='leadership', distill_func=get_none),
]
