# NSNCO-Django-Intern-Assignment
Django Intern Assignment


## Admin:
### Can be created using superuser or use : 
  Username: mayur
  ***
  Pass: 1234
  ***
http://127.0.0.1:8000/admin/

## Api enpoints:

### Works
  http://127.0.0.1:8000/signals/api/works[name='work-list']

### Integrate Filtering with Work Type
 http://127.0.0.1:8000/signals/api/works?work_type=Youtube or pk of YouTube

### Integrate Search with Artist name
  http://127.0.0.1:8000/signals/api/works-by-artist[name='artist-work-list']

### Integrate Registration API with username & password within the body
of the request:
  http://127.0.0.1:8000/signals/api/register[name='register']
