from django.urls import path

from .views import UserProfileView, UserLoginView, UserSignupView, UploadEvaluationResultsView, UploadModuleEvidenceView

urlpatterns = [
    path('api/user/profile/<int:user_id>/', UserProfileView.as_view(), name='user-profile'),
    path('api/user/login/', UserLoginView.as_view(), name='user-login'),
    path('api/user/signup/', UserSignupView.as_view(), name='user-signup'),
    path('api/user/evaluations/', UploadEvaluationResultsView.as_view(), name='upload-evaluation-results'),
    path('api/user/evidences/', UploadModuleEvidenceView.as_view(), name='upload-module-evidence'),
    # Agrega las URLS para las otras vistas aquí
]
