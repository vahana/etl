import logging
import prf

from jobs.views import BaseJobView
from jobs.etl import ETLJob

log = logging.getLogger(__name__)

class ETLJobView(BaseJobView):
    _job_class = ETLJob

