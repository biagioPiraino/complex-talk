# Complex Talk
<h3> Description </h3>
<p> 
  Complex Talk is a blogging web application prototype developed using the <a href="https://flask.palletsprojects.com/en/2.3.x/">Flask Framework.</a>
</p>
<p> 
  Within Complex Talk a user can post and read articles belonging to four different categories: <em>Tech</em>, <em>Business</em>, <em>World</em> and <em>Lifestyle</em>.
</p>
<hr>

<h3>Prerequisites</h3>
Have an active <a href="https://www.postgresql.org/" target="_blank">PostgreSQL</a> server running locally.
<hr>

<h3>How to use</h3>

1) Create an .env file in the projects' root folder containing the following database-related variables:

<table>
  <tr>
    <td>HOST</td>
    <td>PORT</td>
    <td>DB_NAME</td>
    <td>DB_USER</td>
    <td>PASSWORD</td>
    <td>DATE_FORMAT</td>
  </tr>
</table>

2) Create a .venv folder in the projects' root folder and create a virtual environment by running the command <code>$ virtualenv .venv</code>.

3) Install the <a href="https://pypi.org/project/psycopg2/" target="_blank"><em>psycopg2</em></a>, <a href="https://flask.palletsprojects.com/en/2.3.x/installation/" target="_blank"><em>Flask</em></a> and <a href="https://pypi.org/project/python-dotenv/" target="_blank"><em>dotenv</em></a> packages.
   
4) Access to a local PostgreSQL server using <code>$ psql -U postgres</code>.

5) Run the <em>database_script.sql</em> using <code>$ \i path\database_script.sql</code> once connected to the local server.

6) Activate the virtual environment using <code>$ source .venv/bin/activate</code>.

7) Run the <code>init.py</code> script.

<hr>
<h3>References</h3>
<table>
<thead>
  <tr>
    <th>References</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>
      <a href="https://book.pythontips.com/en/latest/virtual_environment.html" target="_blank">Python virtual environments</a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://www.psycopg.org/docs/" target="_blank">Psycopg 2.9.5 documentation</a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://flask.palletsprojects.com/en/2.3.x/" target="_blank">Flask documentation</a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://getbootstrap.com/docs/5.3/getting-started/introduction/" target="_blank">Bootstrap documentation</a>
    </td>
  </tr>
 </tbody>
 </table>
