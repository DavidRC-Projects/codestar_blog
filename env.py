import os
import dj_database_url
if os.path.isfile('env.py'):
    import env

os.environ.setdefault("DATABASE_URL", "postgresql://neondb_owner:npg_qyo6kzAb3Zct@ep-floral-cloud-a2mfbqmv.eu-central-1.aws.neon.tech/breed_sneer_floss_90695?password=crystal2000")

os.environ.setdefault(
    "CLOUDINARY_URL", "cloudinary://382354952571716:HGkNZfiV2Iwi0op-ClZZH4_x7j8@dtyahkut6"
)
