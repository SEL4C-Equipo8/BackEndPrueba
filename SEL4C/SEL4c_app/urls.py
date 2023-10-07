from django.urls import path
from . import views

from .views import UserProfileView, UserLoginView, UserSignupView, UploadEvaluationResultsView, UploadModuleEvidenceView, ActivityDetailView, ModuleDetailView, AdminDetailView, AdminListView, CreateEvaluationView
from .views import AdminLoginView, AdminDashboardView, AdminPersonalProgressView, AdminUsersListView, AdminGenderSegmentationView, AdminAgeSegmentationView, AdminNationalitySegmentationView, AdminEducationSegmentationView
from .views import UserProgressBarsView, UserProgressBriefView, UserProgressInitialEvaluationView, UserProgressFinalEvaluationView, ActivityCreateView, ModuleCreateView, ActivityListView, ModuleListView, UserProgressView
from .views import EstadisticasCreateView, UserProgressActivtiesView, AdminSignupView, AdminLogoutView, PreguntasListView, PreguntasDetailView, RespuestasDetailView

urlpatterns = [
    #####   USER   #####
    # User (login, signup, profile) OK
    path('api/user/profile/<int:user_id>/', UserProfileView.as_view(), name='user-profile'),
    path('api/user/login/', UserLoginView.as_view(), name='user-login'),
    path('api/user/signup/', UserSignupView.as_view(), name='user-signup'),
    #  Evaluations OK
    path('api/user/evaluations/create/', CreateEvaluationView.as_view(), name='upload-evaluation-results'),
    path('api/user/evaluations/', UploadEvaluationResultsView.as_view(), name='upload-evaluation-results'),
    path('api/user/progress/initialEvaluation/<int:id_usuario>/', UserProgressInitialEvaluationView.as_view(), name='user-progress-initial-evaluation'),
    path('api/user/progress/finalEvaluation/<int:id_usuario>/', UserProgressFinalEvaluationView.as_view(), name='user-progress-final-evaluation'),
    # Activities OK 
    path('api/admin/activities/all/', ActivityListView.as_view(), name='activity-list'),
    path('api/admin/activities/<int:id_actividad>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('api/admin/activities/', ActivityCreateView.as_view(), name='activity-detail'),
    # Modules OK
    path('api/admin/activity/<int:id_actividad>/module/all/', ModuleListView.as_view(), name='module-detail'),
    path('api/admin/activity/<int:id_actividad>/module/<int:id_modulo>/', ModuleDetailView.as_view(), name='module-detail'),
    path('api/admin/activity/<int:id_actividad>/module/create/', views.ModuleCreateView, name='module-detail'),
            #OLD VIEW
            # path('api/admin/activity/<int:id_actividad>/module/', ModuleCreateView.as_view(), name='module-detail'),
    # Evidences OK
    path('api/user/evidences/', UploadModuleEvidenceView.as_view(), name='upload-module-evidence'),
    #Estadisticas
    path('api/admin/estadisticas/create/', EstadisticasCreateView.as_view(), name='create-statistics'),
    # Progress App
    path('api/user/progress/activities/<int:id_usuario>/', UserProgressActivtiesView.as_view(), name='user-progress-activities'),
    path('api/user/progress/bars/<int:id_usuario>/', UserProgressBarsView.as_view(), name='user-progress-bars'),
    path('api/user/progress/brief/<int:id_usuario>/', UserProgressBriefView.as_view(), name='user-progress-brief'),
    # ADMIN OK  
    path('api/admin/signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('api/admin/login/',AdminLoginView.as_view(), name='admin-login'),
    path('api/admin/logout/', AdminLogoutView.as_view(), name='admin-logout'),
    path('api/admin/', AdminListView.as_view(), name='admin-list'),
    path('api/admin/<int:id_admin>/', AdminDetailView.as_view(), name='admin-detail'),
    
    # Dashboard
    path('api/progress/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('api/admin/personalProgress/<int:user_id>/', AdminPersonalProgressView.as_view(), name='admin-personal-progress'),
    path('api/admin/users/', AdminUsersListView.as_view(), name='admin-users-list'),
    path('api/admin/segmentation/gender/', AdminGenderSegmentationView.as_view(), name='admin-gender-segmentation'),
    path('api/segmentation/admin/age/', AdminAgeSegmentationView.as_view(), name='admin-age-segmentation'),
    path('api/segmentation/admin/nationality/', AdminNationalitySegmentationView.as_view(), name='admin-nationality-segmentation'),
    path('api/segmentation/admin/education/', AdminEducationSegmentationView.as_view(), name='admin-education-segmentation'),
    # Progreso Usuario
    path('api/user/progress/user/<int:id_usuario>/', UserProgressView.as_view(), name='user-progress'),

    #Who am I?
    path('api/whoami/', views.whoami, name='whoami'),

    #Preguntas
    path('api/preguntas/all/', PreguntasListView.as_view(), name='preguntas-list'),
    path('api/preguntas/<int:id_pregunta>/', PreguntasDetailView.as_view(), name='preguntas-detail'),

    #Respuestas
    path('api/respuestas/<int:id_usuario>/<int:id_evaluacion>/', RespuestasDetailView.as_view(), name='respuestas-detail'),
    
]
