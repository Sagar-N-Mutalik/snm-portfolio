from django_distill import distill_path
from .views import HomeView, ProjectsView, LeadershipView

urlpatterns = [
    # Removed distill_func completely for static pages with no dynamic parameters
    distill_path('', HomeView.as_view(), name='home'),
    distill_path('projects/', ProjectsView.as_view(), name='projects'),
    distill_path('leadership/', LeadershipView.as_view(), name='leadership'),
]