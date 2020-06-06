import logging
import os
from pyramid.config import Configurator
from slovar import slovar

from prf.utils import maybe_dotted

Settings = slovar()
log = logging.getLogger(__name__)


def main(global_config, **settings):
    global Settings
    config = Configurator(settings=settings)

    config.include('prf')
    Settings = config.prf_settings()

    #enables data backends
    config.include('prf.mongodb')
    config.include('prf.es')
    config.include('prf.csv')
    config.include('prf.s3')

    #enables dataset navigation views
    config.include('datasets.views')

    #enables etl job
    config.include('jobs')

    #render for csv files
    config.add_renderer('tab', maybe_dotted('prf.utils.csv.TabRenderer'))


    #enables get tunneling - post,put,delete could be issues using `_m=<method>` as url param.
    #e.g. `_m=POST&abc=123` will issue post with json body {"abc":"123"}
    config.add_tween('prf.tweens.GET_tunneling')

    #defines REST resources

    root = config.get_root_resource()

    jobs = root.add_singular('jobs', view='jobs.views.JobsView')

    jobs.add('__all', '_all', view='jobs.views.JobsView')

    #add resource to etl jobs
    jobs.add('etl_', 'etl', view='etl.views.ETLJobView')

    #add resource for job progress/status
    root.add_singular('job_status', view='jobs.views.JobStatusView')

    return config.make_wsgi_app()

