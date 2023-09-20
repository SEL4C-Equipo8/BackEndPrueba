from django.urls import path

from .views import UserProfileView, UserLoginView, UserSignupView, UploadEvaluationResultsView, UploadModuleEvidenceView, ActivityDetailView, ModuleDetailView, AdminDetailView, AdminListView
from .views import AdminDashboardView, AdminPersonalProgressView, AdminUsersListView, AdminGenderSegmentationView, AdminAgeSegmentationView, AdminNationalitySegmentationView, AdminEducationSegmentationView

urlpatterns = [
    path('api/user/profile/<int:user_id>/', UserProfileView.as_view(), name='user-profile'),
    path('api/user/login/', UserLoginView.as_view(), name='user-login'),
    path('api/user/signup/', UserSignupView.as_view(), name='user-signup'),
    path('api/user/evaluations/', UploadEvaluationResultsView.as_view(), name='upload-evaluation-results'),
    path('api/user/evidences/', UploadModuleEvidenceView.as_view(), name='upload-module-evidence'),
    path('api/admin/activity/<int:id_actividad>/module/<int:id_modulo>/', ModuleDetailView.as_view(), name='module-detail'),
    path('api/admin/', AdminListView.as_view(), name='admin-list'),
    path('api/admin/<int:id_admin>/', AdminDetailView.as_view(), name='admin-detail'),
    path('api/progress', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('api/admin/personalProgress/<int:user_id>/', AdminPersonalProgressView.as_view(), name='admin-personal-progress'),
    path('api/admin/users/', AdminUsersListView.as_view(), name='admin-users-list'),
    path('api/admin/segmentation/gender', AdminGenderSegmentationView.as_view(), name='admin-gender-segmentation'),
    path('api/segmentation/admin/age', AdminAgeSegmentationView.as_view(), name='admin-age-segmentation'),
    path('api/segmentation/admin/nationality', AdminNationalitySegmentationView.as_view(), name='admin-nationality-segmentation'),
    path('api/segmentation/admin/education', AdminEducationSegmentationView.as_view(), name='admin-education-segmentation'),
]
