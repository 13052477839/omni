"""
Copyright 2017 Platform9 Systems Inc.(http://www.platform9.com)
Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
"""

from oslo_config import cfg

azure_group = cfg.OptGroup(name='azure',
                           title='Options to connect to Azure cloud')

azure_opts = [
    cfg.StrOpt('tenant_id', help='Tenant id of Azure account'),
    cfg.StrOpt('client_id', help='Azure client id'),
    cfg.StrOpt('client_secret', help='Azure client secret', secret=True),
    cfg.StrOpt('subscription_id', help='Azure subscription id'),
    cfg.StrOpt('region', help='Azure region'),
    cfg.StrOpt('resource_group', help="Azure resource group"),
    cfg.StrOpt('azure_pool_name', help='Azure pool name', default='azure'),
    cfg.IntOpt('azure_free_capacity_gb',
               help='Free space available on Azure storage pool',
               default=1024),
    cfg.IntOpt('azure_total_capacity_gb',
               help='Total space available on Azure storage pool',
               default=1024)
]

cfg.CONF.register_group(azure_group)
cfg.CONF.register_opts(azure_opts, group=azure_group)

tenant_id = cfg.CONF.azure.tenant_id
client_id = cfg.CONF.azure.client_id
client_secret = cfg.CONF.azure.client_secret
subscription_id = cfg.CONF.azure.subscription_id
region = cfg.CONF.azure.region
resource_group = cfg.CONF.azure.resource_group
azure_pool_name = cfg.CONF.azure.azure_pool_name
azure_free_capacity_gb = cfg.CONF.azure.azure_free_capacity_gb
azure_total_capacity_gb = cfg.CONF.azure.azure_total_capacity_gb
