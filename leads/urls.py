from rest_framework import routers

from .api import LeadViewsets, userviewsets, formviewsets, chatviewsets

router = routers.DefaultRouter()
router.register('api/leads', LeadViewsets, 'leads')
router.register('api/users', userviewsets, 'users')
router.register('api/forms', formviewsets, 'forms')
router.register('api/messages', chatviewsets, 'chat')
urlpatterns = router.urls
