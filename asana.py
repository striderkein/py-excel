from cv2 import HOGDESCRIPTOR_DEFAULT_NLEVELS

import asana

client = asana.Client.access_token('PERSONAL_ACCESS_TOKEN')
workspace_gid = 1196247230098161

result = client.typeahead.typeahead_for_workspace(workspace_gid, {'param': 'value', 'param': 'value'}, opt_pretty=True)
print(result)
