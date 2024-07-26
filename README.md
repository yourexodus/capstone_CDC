<p align="center"> 
  <img src="images/Logo.PNG" alt="Logo.PNG" width="80px" height="80px">
</p>
<h1 align="center"> Diabetis Predictor </h1>
<h3 align="center"> Python Developer Capstone 1</h3>
<h5 align="center"> Python Developer Career Training Course <a href="https://www.nwmissouri.edu/pdcenter/courses/python-developer.htm">Northwest Missouri State University</a>  (2024) </h5>

<p align="center"> 
<img src="gif/MeowMidwest.gif" alt="MeowMidwest" height="382px">
</p>

<p>I have built a Supervised Learning Classification model to predict the probabilty of diabetis given age and physical activity data.  Will be using Python to feed data into my Machine Learning model to obtain my diabetes prediction.</p>

<h2>Workflow: </h2>
<ul>
   
  <li><p>Frame my Hypothesis: </p>
      <p>Increase exercise and healthier eating habits can lessen the probabilty of developing diabetes for all ages</p>
  </li>
  <li><p>Prepare my data: <a href="https://github.com/yourexodus/capstone_CDC/blob/469596f51d067db56879acb643a9940d63df5f2b/GettingToKnowTheData.ipynb">GettingToKnowTheData</a></p>   
      <p> Jupyter Notebook</p>
  </li>
  <li><p>Analyze using visuals and make some determinations: <a href="https://github.com/yourexodus/capstone_CDC/blob/469596f51d067db56879acb643a9940d63df5f2b/Visualizing%20and%20Interpreting%20Data.ipynb">Visualizing and Interpretting Data</a></p>   
      <p> Jupyter Notebook</p>
  </li>
   
  <li><p>Replaced Codes with Label names.  Saved to file: <a href="https://github.com/yourexodus/capstone_CDC/blob/0efb2177b9301e45ff95de6d289d66fc38282c6f/Feature_Engineering.ipynb">Feature_Engineering</a></p>
      <p> Jupyter Notebook</p>
  </li>
  <li><p>Communicate Results -- Added Notes in files.  Emailed. Feedback Received 07/24</p>
      <p> Jupyter Notebook</p>
     
  </li>

<li><p>Logistic and Random Forest: <a href="https://github.com/yourexodus/capstone_CDC/blob/339cba065dcbb70e7bb0a1fa995e8596e2f7c367/Modeling.ipynb">Modeling</a></p>   
      <p> Jupyter Notebook</p>
  </li>
  <li><p>Pickle the model: <a href="https://github.com/yourexodus/capstone_CDC/blob/main/Score_New_Data.ipynb">Score New Data</a></p>         
       <p> Jupyter Notebook</p>
  </li>
  <li><p>Build my app -- 07/25 in-progres</p>
      <p> Pycharm:  transfer jupyter notebook ipynb files to py files
      <p> Pycharm:  Make visuals interactive by converting them Dash Plotly </p>
      <p> Pycharm: Launch app to render.com </p>
      
  </li>
</ul>

<ul
<h2>References</h2>
<ul>
  <img src="images/sites.PNG" alt="sites" height="50px"> 
  <li><p>Design Inspiration, Author:Mohammad Amin Shamshiri </p>
      <p>link: https://raw.githubusercontent.com/yourexodus/Spam-Detector/master/README.md</p>
  </li>
  <li><p> </p>
      <p>link:  </p>
  </li>
  <li><p>Gemini - Used AI to generate cat Images and to learn How to deploy my Prediction model</p>
      <p>link:  https://gemini.google.com</p>
  </li>
  <li><p>Canva,  create my gif file using my cat images from Gemini</p>
      <p>link: https://www.canva.com </p>
  </li>
  <li><p>Udemy.com - Online course </p>
      <p>course:How to use ChatGPT and Generative AI to help create content</p>
      <p>course:Deployment of Machine Learning Models</p>
      <img src="images/PackageCodeIntoModule.png" alt="Inspired" height="382px">
      <img src="images/WorkFlow.png" alt="Inspired" height="382px">
  
  </li>
  <li><p> </p>
      <p> </p>
  </li>
</ul>
<h2> Available CDC Data </h2> 
<ul>
       https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators  <br>
       	https://archive.ics.uci.edu/static/public/891/data.csv* <br>
        https://www.cdc.gov/brfss/annual_data/annual_2014.html   <br> 
         https://www.cdc.gov/brfss/annual_data/2014/pdf/CODEBOOK14_LLCP.pdf  
  <br>
  


</ul>

 <H2>Data Codes</H2>
<ul>
<table>
  <thead>
    <tr>
      <th>Data: Education Level codes:</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1 Never attended school or only kindergarten</td>
    </tr>
    <tr>
      <td>2 Grades 1 through 8 (Elementary)</td>
    </tr>
    <tr>
      <td>3 Grades 9 through 11 (Some high school)</td>
    </tr>
    <tr>
      <td>4 Grade 12 or GED (High school graduate)</td>
    </tr>
    <tr>
      <td>5 College 1 year to 3 years (Some college or technical school)</td>
    </tr>
    <tr>
      <td>6 College 4 years or more (College graduate)</td>
    </tr>
    <tr>
      <td>9 Refused</td>
    </tr>
    <tr>
      <td>BLANK Not asked or Missing 1,770</td>
    </tr>
  </tbody>
</table>



<table>
  <thead>
    <tr>
      <th>General Health Codes</th>
      <th>Mental health code</th>
      <th>Number of Days Physical Health Not Good</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1 Excellent</td>
      <td>1 - 30 Number of days</td>
      <td>1 - 30 Number of days</td>
    </tr>
    <tr>
      <td>2 Very good</td>
      <td>88 None</td>
      <td>88 None</td>
    </tr>
    <tr>
      <td>3 Good</td>
      <td>77 Don’t know/Not sure</td>
      <td>77 Don’t know</td>
    </tr>
    <tr>
      <td>4 Fair</td>
      <td>99 Refused</td>
      <td>99 Refused</td>
    </tr>
    <tr>
      <td>5 Poor</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>7 Don’t</td>
      <td>know/Not Sure</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>9 Refused</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>


<table>
  <thead>
    <tr>
      <th>Difficulty Walking or Climbing Stairs (DiffWalk)</th>
      <th>Income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1 - 30 Number of days</td>
      <td>1  - Less than $10,000</td>
    </tr>
    <tr>
      <td>88 None</td>
      <td>2  - Less than $15,000 ($10,000 to less than $15,000)</td>
    </tr>
    <tr>
      <td>77 Don’t know/Not sure</td>
      <td>3  - Less than $20,000 ($15,000 to less than $20,000)</td>
    </tr>
    <tr>
      <td>99 Refused</td>
      <td>4  - Less than $25,000 ($20,000 to less than $25,000)</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>5 -  Less than $35,000 ($25,000 to less than $35,000)</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>6  - Less than $50,000 ($35,000 to less than $50,000)</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>7 - Less than $75,000 ($50,000 to less than $75,000)</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>8  - $75,000 or more</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>77 -  Don’t know/Not sure</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>99  - Refused</td>
    </tr>
  </tbody>
</table>
</ul>
<h2>My Journal</h2>
<ul>
<table>
  <thead>
    <tr>
      <th>Date</th>
      <th>progress</th>
      <th>accomplishment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>07/22</td>
      <td>Capstone project was approved.  worked on importing data setting up environment: git, github, jupyter notebook.  Created new repository</td>
      <td>Overcame SSH errors when using commit line cmd.  Just decided to upload my files to my repository</td>
    </tr>
    <tr>
      <td>07/23</td>
      <td>I used AI to generate images .  Super cool! I had a lot of trial and error.  I decided just to take crash course on udemy how to do it.</td>
      <td>Created a git file</td>
    </tr>
    <tr>
      <td>07/24</td>
      <td>Worked on exploring my data and researching techniques to saving model for scoring of new data</td>
      <td>Created 3 jupyter notebook files</td>
    </tr>
    <tr>
      <td>07/25</td>
      <td>Feature engineering my data by adding labels and export files I can use in a dashboard. continuation of what I learned yesterday in saving my model to a pickle file in 1 notebook and load and use it in another.     When I reloaded, I only reloaded my Random Forest model because it out performed my logistic model.</td>
      <td>Created more jupyter notebook files.  Figured out how to save & Reloaded & score new data using Pickle files</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>
</ul>
