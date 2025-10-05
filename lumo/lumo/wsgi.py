import os
from django.core.wsgi import get_wsgi_application

print("=== WSGI STARTUP ===")
print("1. Setting Django settings module...")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumo.settings')

print("2. Settings module set, creating application...")

try:
    application = get_wsgi_application()
    print("3. WSGI application created successfully!")
    print("=== APPLICATION READY ===")
except Exception as e:
    print(f"ERROR creating WSGI application: {e}")
    print(f"Error type: {type(e)}")
    import traceback
    traceback.print_exc()
    raise