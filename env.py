import os
import dj_database_url
if os.path.isfile('env.py'):
    import env

os.environ.setdefault("DATABASE_URL", "postgresql://neondb_owner:npg_qyo6kzAb3Zct@ep-floral-cloud-a2mfbqmv.eu-central-1.aws.neon.tech/breed_sneer_floss_90695?password=crystal2000")

