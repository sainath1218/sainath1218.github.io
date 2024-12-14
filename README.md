# sainath1218.github.io
Titanic Analysis

1. Problem Space (Clarification of the Problem Space)
What: The goal of this project is to analyze the Titanic dataset to identify factors that influenced passenger survival during the tragic sinking of the ship in 1912.
Why: Understanding these factors provides insights into historical decisions and survival patterns, which can have educational value and relevance for disaster management studies.
Who: This analysis is useful for historians, sociologists, and educators interested in understanding human behavior in disaster scenarios.
Where: The data focuses on passengers aboard the RMS Titanic, a transatlantic ocean liner.
When: The dataset covers the period of the ship's voyage in 1912.

2. Questions to Address through Data Analysis
What was the survival rate of passengers on the Titanic?
How did gender affect survival rates?
Was there a significant difference in survival rates among different passenger classes (Pclass)?
Did the age of passengers influence their chances of survival?
Were passengers who embarked from different ports (Embarked) more or less likely to survive?
What was the correlation between having family members on board (SibSp and Parch) and survival rates?

3. Understanding of Dataset
Data Source: The Titanic dataset is publicly available on Kaggle and contains detailed information about the passengers aboard the RMS Titanic.

Dataset Description: The dataset includes fields such as:
Survived: Survival status (1 = Survived, 0 = Did not survive).
Pclass: Passenger class (1st, 2nd, or 3rd).
Sex: Gender of the passenger.
Age: Age of the passenger.
SibSp and Parch: Number of family members onboard.
Embarked: Port of embarkation (C = Cherbourg, Q = Queenstown, S = Southampton).

Dataset Relevance:
The dataset provides all the necessary variables to analyze factors influencing survival rates, such as gender, age, passenger class, and family relationships.


Questions and Answers
1.	What is the overall survival rate of Titanic passengers?
Answer: Based on the Survived column, the survival rate is approximately 38%, 
2.	How does gender affect the survival rate?
Answer: Grouped analysis shows that female passengers had a significantly higher survival rate than male passengers, indicating a priority for rescuing women during the evacuation. This indicates that the priority of rescue for women is higher than that for men
3.	Is there a significant difference in survival rates across different passenger classes (Pclass)?
Answer: Survival rates are notably higher for passengers in higher classes (especially 1st class). This suggests that passenger class influenced rescue priority. It could be proximity to the lifeboats or social norms. 
4.	Does age influence survival rate?
Answer: Boxplots or age distribution analysis reveal that younger passengers (especially children) had a higher survival rate.
5.	What is the impact of embarkation ports (Embarked) on survival rates?
Answer: Grouped statistics show that passengers who embarked from Cherbourg (C) had the highest survival rate, possibly due to a higher concentration of first-class passengers from this port.
6.	Did traveling with family affect survival rates?
Answer: Grouped analysis based on the combined values of SibSp and Parch indicates that passengers with a moderate number of family members had a higher survival rate, while those traveling alone or with many family members had lower survival rates. Medium-sized families may be better helped during the evacuation process or because family members help each other.


Titanic data analysis summary report

Data background
Titanic data set contains the basic information of passengers and survival labels for analyzing the factors affecting the survival rate.

Key finding

Female passengers have a significantly higher survival rate than male passengers.
The survival rate of first class passengers is significantly higher than that of other classes.

The survival rate for child passengers is better than average.

The port of embarkation (Cherbourg) has the highest survival rate for passengers.

Data support

Charts and data presentations (e.g., survival charts, sex and survival charts, etc.).

Conclusion

The main influencing factors of survival rate include sex, cabin and age. These factors may play an important role in prioritizing rescue decisions in a disaster.


<!DOCTYPE html>


<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <title>d280ffd4b0c949f0b2faa707c0171910</title>
  <style>
    html {
      line-height: 1.5;
      font-family: Georgia, serif;
      font-size: 20px;
      color: #1a1a1a;
      background-color: #fdfdfd;
    }
    body {
      margin: 0 auto;
      max-width: 36em;
      padding-left: 50px;
      padding-right: 50px;
      padding-top: 50px;
      padding-bottom: 50px;
      hyphens: auto;
      overflow-wrap: break-word;
      text-rendering: optimizeLegibility;
      font-kerning: normal;
    }
    @media (max-width: 600px) {
      body {
        font-size: 0.9em;
        padding: 1em;
      }
      h1 {
        font-size: 1.8em;
      }
    }
    @media print {
      body {
        background-color: transparent;
        color: black;
        font-size: 12pt;
      }
      p, h2, h3 {
        orphans: 3;
        widows: 3;
      }
      h2, h3, h4 {
        page-break-after: avoid;
      }
    }
    p {
      margin: 1em 0;
    }
    a {
      color: #1a1a1a;
    }
    a:visited {
      color: #1a1a1a;
    }
    img {
      max-width: 100%;
    }
    h1, h2, h3, h4, h5, h6 {
      margin-top: 1.4em;
    }
    h5, h6 {
      font-size: 1em;
      font-style: italic;
    }
    h6 {
      font-weight: normal;
    }
    ol, ul {
      padding-left: 1.7em;
      margin-top: 1em;
    }
    li > ol, li > ul {
      margin-top: 0;
    }
    blockquote {
      margin: 1em 0 1em 1.7em;
      padding-left: 1em;
      border-left: 2px solid #e6e6e6;
      color: #606060;
    }
    code {
      font-family: Menlo, Monaco, 'Lucida Console', Consolas, monospace;
      font-size: 85%;
      margin: 0;
    }
    pre {
      margin: 1em 0;
      overflow: auto;
    }
    pre code {
      padding: 0;
      overflow: visible;
      overflow-wrap: normal;
    }
    .sourceCode {
     background-color: transparent;
     overflow: visible;
    }
    hr {
      background-color: #1a1a1a;
      border: none;
      height: 1px;
      margin: 1em 0;
    }
    table {
      margin: 1em 0;
      border-collapse: collapse;
      width: 100%;
      overflow-x: auto;
      display: block;
      font-variant-numeric: lining-nums tabular-nums;
    }
    table caption {
      margin-bottom: 0.75em;
    }
    tbody {
      margin-top: 0.5em;
      border-top: 1px solid #1a1a1a;
      border-bottom: 1px solid #1a1a1a;
    }
    th {
      border-top: 1px solid #1a1a1a;
      padding: 0.25em 0.5em 0.25em 0.5em;
    }
    td {
      padding: 0.125em 0.5em 0.25em 0.5em;
    }
    header {
      margin-bottom: 4em;
      text-align: center;
    }
    #TOC li {
      list-style: none;
    }
    #TOC ul {
      padding-left: 1.3em;
    }
    #TOC > ul {
      padding-left: 0;
    }
    #TOC a:not(:hover) {
      text-decoration: none;
    }
    code{white-space: pre-wrap;}
    span.smallcaps{font-variant: small-caps;}
    div.columns{display: flex; gap: min(4vw, 1.5em);}
    div.column{flex: auto; overflow-x: auto;}
    div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
    ul.task-list{list-style: none;}
    ul.task-list li input[type="checkbox"] {
      width: 0.8em;
      margin: 0 0.8em 0.2em -1.6em;
      vertical-align: middle;
    }
    pre > code.sourceCode { white-space: pre; position: relative; }
    pre > code.sourceCode > span { display: inline-block; line-height: 1.25; }
    pre > code.sourceCode > span:empty { height: 1.2em; }
    .sourceCode { overflow: visible; }
    code.sourceCode > span { color: inherit; text-decoration: inherit; }
    div.sourceCode { margin: 1em 0; }
    pre.sourceCode { margin: 0; }
    @media screen {
    div.sourceCode { overflow: auto; }
    }
    @media print {
    pre > code.sourceCode { white-space: pre-wrap; }
    pre > code.sourceCode > span { text-indent: -5em; padding-left: 5em; }
    }
    pre.numberSource code
      { counter-reset: source-line 0; }
    pre.numberSource code > span
      { position: relative; left: -4em; counter-increment: source-line; }
    pre.numberSource code > span > a:first-child::before
      { content: counter(source-line);
        position: relative; left: -1em; text-align: right; vertical-align: baseline;
        border: none; display: inline-block;
        -webkit-touch-callout: none; -webkit-user-select: none;
        -khtml-user-select: none; -moz-user-select: none;
        -ms-user-select: none; user-select: none;
        padding: 0 4px; width: 4em;
        color: #aaaaaa;
      }
    pre.numberSource { margin-left: 3em; border-left: 1px solid #aaaaaa;  padding-left: 4px; }
    div.sourceCode
      {   }
    @media screen {
    pre > code.sourceCode > span > a:first-child::before { text-decoration: underline; }
    }
    code span.al { color: #ff0000; font-weight: bold; } /* Alert */
    code span.an { color: #60a0b0; font-weight: bold; font-style: italic; } /* Annotation */
    code span.at { color: #7d9029; } /* Attribute */
    code span.bn { color: #40a070; } /* BaseN */
    code span.bu { color: #008000; } /* BuiltIn */
    code span.cf { color: #007020; font-weight: bold; } /* ControlFlow */
    code span.ch { color: #4070a0; } /* Char */
    code span.cn { color: #880000; } /* Constant */
    code span.co { color: #60a0b0; font-style: italic; } /* Comment */
    code span.cv { color: #60a0b0; font-weight: bold; font-style: italic; } /* CommentVar */
    code span.do { color: #ba2121; font-style: italic; } /* Documentation */
    code span.dt { color: #902000; } /* DataType */
    code span.dv { color: #40a070; } /* DecVal */
    code span.er { color: #ff0000; font-weight: bold; } /* Error */
    code span.ex { } /* Extension */
    code span.fl { color: #40a070; } /* Float */
    code span.fu { color: #06287e; } /* Function */
    code span.im { color: #008000; font-weight: bold; } /* Import */
    code span.in { color: #60a0b0; font-weight: bold; font-style: italic; } /* Information */
    code span.kw { color: #007020; font-weight: bold; } /* Keyword */
    code span.op { color: #666666; } /* Operator */
    code span.ot { color: #007020; } /* Other */
    code span.pp { color: #bc7a00; } /* Preprocessor */
    code span.sc { color: #4070a0; } /* SpecialChar */
    code span.ss { color: #bb6688; } /* SpecialString */
    code span.st { color: #4070a0; } /* String */
    code span.va { color: #19177c; } /* Variable */
    code span.vs { color: #4070a0; } /* VerbatimString */
    code span.wa { color: #60a0b0; font-weight: bold; font-style: italic; } /* Warning */
    .display.math{display: block; text-align: center; margin: 0.5rem auto;}
  </style>
  <!--[if lt IE 9]>
    <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv-printshiv.min.js"></script>
  <![endif]-->
</head>
<body>
<div id="EN20ESJ21YJR" class="cell markdown" id="EN20ESJ21YJR">
<p>import libraries</p>
</div>
<div id="mqANy_aa28sp" class="cell code" data-execution_count="3"
id="mqANy_aa28sp">
<div class="sourceCode" id="cb1"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> pandas <span class="im">as</span> pd</span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> seaborn <span class="im">as</span> sns</span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> matplotlib.pyplot <span class="im">as</span> plt</span></code></pre></div>
</div>
<div id="RRIo9g7i3JJd" class="cell markdown" id="RRIo9g7i3JJd">
<p>""" Project: Titanic Survival Analysis Author: Shiping Yu, Tianhao
Wang, Bohan Yang, Andrew Xu, Sainath sunkara</p>
<p>Description: This project analyzes the Titanic dataset to identify
key factors influencing passenger survival rates. The dataset includes
demographic information, ticket class, and survival status of the
passengers.</p>
<p>Key Questions to Address:</p>
<ol>
<li>What is the overall survival rate?</li>
<li>How does gender influence survival rates?</li>
<li>What are the survival rates for different passenger classes?</li>
<li>Does age impact the likelihood of survival?</li>
<li>Is there a relationship between the port of embarkation and survival
rate?</li>
<li>Does the number of family members aboard influence survival?
"""</li>
</ol>
</div>
<div id="CsR72RcV3Jer" class="cell markdown" id="CsR72RcV3Jer">
<h1 id="step-1-load-the-dataset">Step 1: Load the dataset</h1>
</div>
<div id="24mLiZcC3Hjv" class="cell code" data-execution_count="4"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}"
id="24mLiZcC3Hjv" data-outputId="9644c995-2cb9-443b-dd32-7bbdb2fc08ca">
<div class="sourceCode" id="cb2"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a>data <span class="op">=</span> pd.read_csv(<span class="st">&#39;titanic.csv&#39;</span>)</span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(data.head())</span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(data.info())</span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(data.describe())</span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(data.isnull().<span class="bu">sum</span>())</span></code></pre></div>
<div class="output stream stdout">
<pre><code>   PassengerId  Survived  Pclass  \
0            1         0       3   
1            2         1       1   
2            3         1       3   
3            4         1       1   
4            5         0       3   

                                                Name     Sex   Age  SibSp  \
0                            Braund, Mr. Owen Harris    male  22.0      1   
1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
2                             Heikkinen, Miss. Laina  female  26.0      0   
3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
4                           Allen, Mr. William Henry    male  35.0      0   

   Parch            Ticket     Fare Cabin Embarked  
0      0         A/5 21171   7.2500   NaN        S  
1      0          PC 17599  71.2833   C85        C  
2      0  STON/O2. 3101282   7.9250   NaN        S  
3      0            113803  53.1000  C123        S  
4      0            373450   8.0500   NaN        S  
&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    object 
 4   Sex          891 non-null    object 
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    object 
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    object 
 11  Embarked     889 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 83.7+ KB
None
       PassengerId    Survived      Pclass         Age       SibSp  \
count   891.000000  891.000000  891.000000  714.000000  891.000000   
mean    446.000000    0.383838    2.308642   29.699118    0.523008   
std     257.353842    0.486592    0.836071   14.526497    1.102743   
min       1.000000    0.000000    1.000000    0.420000    0.000000   
25%     223.500000    0.000000    2.000000   20.125000    0.000000   
50%     446.000000    0.000000    3.000000   28.000000    0.000000   
75%     668.500000    1.000000    3.000000   38.000000    1.000000   
max     891.000000    1.000000    3.000000   80.000000    8.000000   

            Parch        Fare  
count  891.000000  891.000000  
mean     0.381594   32.204208  
std      0.806057   49.693429  
min      0.000000    0.000000  
25%      0.000000    7.910400  
50%      0.000000   14.454200  
75%      0.000000   31.000000  
max      6.000000  512.329200  
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
</code></pre>
</div>
</div>
<div id="ZHY5rrRJ3Jwb" class="cell markdown" id="ZHY5rrRJ3Jwb">
<h1 id="step-2-data-cleaning">Step 2: Data Cleaning</h1>
</div>
<div id="ZsH1LEq03H5P" class="cell code" data-execution_count="5"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}"
id="ZsH1LEq03H5P" data-outputId="86520d86-f06a-448f-c3d7-4cddf691b5ca">
<div class="sourceCode" id="cb4"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a>data[<span class="st">&#39;Age&#39;</span>] <span class="op">=</span> data[<span class="st">&#39;Age&#39;</span>].fillna(data[<span class="st">&#39;Age&#39;</span>].median())</span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a>data[<span class="st">&#39;Embarked&#39;</span>] <span class="op">=</span> data[<span class="st">&#39;Embarked&#39;</span>].fillna(data[<span class="st">&#39;Embarked&#39;</span>].mode()[<span class="dv">0</span>])</span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a>data.drop(columns<span class="op">=</span>[<span class="st">&#39;Cabin&#39;</span>], inplace<span class="op">=</span><span class="va">True</span>)</span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a>data.drop_duplicates(inplace<span class="op">=</span><span class="va">True</span>)</span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(data.isnull().<span class="bu">sum</span>())</span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a>data.to_csv(<span class="st">&#39;cleaned_titanic.csv&#39;</span>, index<span class="op">=</span><span class="va">False</span>)</span></code></pre></div>
<div class="output stream stdout">
<pre><code>PassengerId    0
Survived       0
Pclass         0
Name           0
Sex            0
Age            0
SibSp          0
Parch          0
Ticket         0
Fare           0
Embarked       0
dtype: int64
</code></pre>
</div>
</div>
<div id="pIFy6j-B3J_-" class="cell markdown" id="pIFy6j-B3J_-">
<h1 id="step-3-exploratory-data-analysis-eda">Step 3: Exploratory Data
Analysis (EDA)</h1>
</div>
<div id="G9-uwP0I3z_M" class="cell markdown" id="G9-uwP0I3z_M">
<h1 id="visualize-survival-count">Visualize survival count</h1>
</div>
<div id="yRHvqxxx3ICG" class="cell code" data-execution_count="6"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}"
id="yRHvqxxx3ICG" data-outputId="30c98d5c-3a26-4287-c673-4034963231dc">
<div class="sourceCode" id="cb6"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb6-1"><a href="#cb6-1" aria-hidden="true" tabindex="-1"></a>sns.countplot(x<span class="op">=</span><span class="st">&#39;Survived&#39;</span>, data<span class="op">=</span>data)</span>
<span id="cb6-2"><a href="#cb6-2" aria-hidden="true" tabindex="-1"></a>plt.title(<span class="st">&#39;Survival Count&#39;</span>)</span>
<span id="cb6-3"><a href="#cb6-3" aria-hidden="true" tabindex="-1"></a>plt.show()</span></code></pre></div>
<div class="output display_data">
<p><img
src="b6a67c90903c2ecc9af0786e3d0464af97fde15a.png" /></p>
</div>
</div>
<div id="Zfz_PUrc4KvA" class="cell markdown" id="Zfz_PUrc4KvA">
<h1 id="visualize-passenger-class-distribution">Visualize passenger
class distribution</h1>
</div>
<div id="j6mO3WBh4KIQ" class="cell code" data-execution_count="7"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}"
id="j6mO3WBh4KIQ" data-outputId="653b7a3b-a9ed-49c8-ec11-f6c239e7f806">
<div class="sourceCode" id="cb7"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb7-1"><a href="#cb7-1" aria-hidden="true" tabindex="-1"></a>sns.countplot(x<span class="op">=</span><span class="st">&#39;Pclass&#39;</span>, data<span class="op">=</span>data)</span>
<span id="cb7-2"><a href="#cb7-2" aria-hidden="true" tabindex="-1"></a>plt.title(<span class="st">&#39;Passenger Class Distribution&#39;</span>)</span>
<span id="cb7-3"><a href="#cb7-3" aria-hidden="true" tabindex="-1"></a>plt.show()</span></code></pre></div>
<div class="output display_data">
<p><img
src="6193b0a018b64d2a2fe7761bd53561b4aee5dcbd.png" /></p>
</div>
</div>
<div id="7-6JFtG84LA4" class="cell markdown" id="7-6JFtG84LA4">
<h1 id="visualize-gender-distribution">Visualize gender
distribution</h1>
</div>
<div id="swJ9R-1i4aCR" class="cell code" data-execution_count="8"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}"
id="swJ9R-1i4aCR" data-outputId="3c34dc96-3a4f-409b-85d5-94158e9b2afb">
<div class="sourceCode" id="cb8"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb8-1"><a href="#cb8-1" aria-hidden="true" tabindex="-1"></a>sns.countplot(x<span class="op">=</span><span class="st">&#39;Sex&#39;</span>, data<span class="op">=</span>data)</span>
<span id="cb8-2"><a href="#cb8-2" aria-hidden="true" tabindex="-1"></a>plt.title(<span class="st">&#39;Gender Distribution&#39;</span>)</span>
<span id="cb8-3"><a href="#cb8-3" aria-hidden="true" tabindex="-1"></a>plt.show()</span></code></pre></div>
<div class="output display_data">
<p><img
src="vertopal_02cd93c0ceb54a44986da2c869cef483/72fcaee2793b98cf34280c1f787f958399c1b664.png" /></p>
</div>
</div>
<div id="OFoBp66t4LHL" class="cell markdown" id="OFoBp66t4LHL">
<h1 id="visualize-embarkation-port-distribution">Visualize embarkation
port distribution</h1>
</div>
<div id="WA5x9qLg4ryr" class="cell code" data-execution_count="9"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}"
id="WA5x9qLg4ryr" data-outputId="63e1457c-ae70-4ff2-f09f-871c544d2886">
<div class="sourceCode" id="cb9"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb9-1"><a href="#cb9-1" aria-hidden="true" tabindex="-1"></a>sns.countplot(x<span class="op">=</span><span class="st">&#39;Embarked&#39;</span>, data<span class="op">=</span>data)</span>
<span id="cb9-2"><a href="#cb9-2" aria-hidden="true" tabindex="-1"></a>plt.title(<span class="st">&#39;Embarkation Port Distribution&#39;</span>)</span>
<span id="cb9-3"><a href="#cb9-3" aria-hidden="true" tabindex="-1"></a>plt.show()</span></code></pre></div>
<div class="output display_data">
<p><img
src="vertopal_02cd93c0ceb54a44986da2c869cef483/83f5fa483758d951217375eb2e9b2985076783d5.png" /></p>
</div>
</div>
<div id="Snt31FfY4LK3" class="cell markdown" id="Snt31FfY4LK3">
<h1 id="visualize-age-distribution">Visualize age distribution</h1>
</div>
<div id="yXVAC1sV4rrj" class="cell code" data-execution_count="10"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}"
id="yXVAC1sV4rrj" data-outputId="f07074a2-d18c-4a5e-9134-58d7fe5c89d1">
<div class="sourceCode" id="cb10"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb10-1"><a href="#cb10-1" aria-hidden="true" tabindex="-1"></a>sns.histplot(data[<span class="st">&#39;Age&#39;</span>], kde<span class="op">=</span><span class="va">True</span>, bins<span class="op">=</span><span class="dv">30</span>)</span>
<span id="cb10-2"><a href="#cb10-2" aria-hidden="true" tabindex="-1"></a>plt.title(<span class="st">&#39;Age Distribution&#39;</span>)</span>
<span id="cb10-3"><a href="#cb10-3" aria-hidden="true" tabindex="-1"></a>plt.show()</span></code></pre></div>
<div class="output display_data">
<p><img
src="vertopal_02cd93c0ceb54a44986da2c869cef483/610ab7adfbd1c355498bede24e121693c37c3c0f.png" /></p>
</div>
</div>
<div id="sYaS2ePS4LN9" class="cell markdown" id="sYaS2ePS4LN9">
<h1 id="visualize-fare-distribution">Visualize fare distribution</h1>
</div>
<div id="UIUseKNt4rbk" class="cell code" data-execution_count="11"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}"
id="UIUseKNt4rbk" data-outputId="199fc30f-f42d-4c14-dc4a-ae6c4645d29b">
<div class="sourceCode" id="cb11"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb11-1"><a href="#cb11-1" aria-hidden="true" tabindex="-1"></a>sns.histplot(data[<span class="st">&#39;Fare&#39;</span>], kde<span class="op">=</span><span class="va">True</span>, bins<span class="op">=</span><span class="dv">30</span>)</span>
<span id="cb11-2"><a href="#cb11-2" aria-hidden="true" tabindex="-1"></a>plt.title(<span class="st">&#39;Fare Distribution&#39;</span>)</span>
<span id="cb11-3"><a href="#cb11-3" aria-hidden="true" tabindex="-1"></a>plt.show()</span></code></pre></div>
<div class="output display_data">
<p><img
src="vertopal_02cd93c0ceb54a44986da2c869cef483/4d28f396c93c733cad75be52b61deb21aa937408.png" /></p>
</div>
</div>
<div id="UszDsXoh4LgO" class="cell markdown" id="UszDsXoh4LgO">
<h1 id="survival-rate-by-gender">Survival rate by gender</h1>
</div>
<div id="XY7C9YOX3II5" class="cell code" data-execution_count="12"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}"
id="XY7C9YOX3II5" data-outputId="1e87c181-2fa9-41f2-a15b-0dbda9a9d48a">
<div class="sourceCode" id="cb12"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb12-1"><a href="#cb12-1" aria-hidden="true" tabindex="-1"></a>sns.barplot(x<span class="op">=</span><span class="st">&#39;Sex&#39;</span>, y<span class="op">=</span><span class="st">&#39;Survived&#39;</span>, data<span class="op">=</span>data)</span>
<span id="cb12-2"><a href="#cb12-2" aria-hidden="true" tabindex="-1"></a>plt.title(<span class="st">&#39;Survival Rate by Gender&#39;</span>)</span>
<span id="cb12-3"><a href="#cb12-3" aria-hidden="true" tabindex="-1"></a>plt.show()</span></code></pre></div>
<div class="output display_data">
<p><img
src="vertopal_02cd93c0ceb54a44986da2c869cef483/dc3de73f5609c91e5971591fc3f2cb74cace80a9.png" /></p>
</div>
</div>
<div id="Hya3Lphj5Qtb" class="cell markdown" id="Hya3Lphj5Qtb">
<h1 id="survival-rate-by-passenger-class">Survival rate by passenger
class</h1>
</div>
<div id="AyNhjuKg5Ssc" class="cell code" data-execution_count="13"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}"
id="AyNhjuKg5Ssc" data-outputId="795122b5-18c5-48f1-8fdb-aeb2dada0b7b">
<div class="sourceCode" id="cb13"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb13-1"><a href="#cb13-1" aria-hidden="true" tabindex="-1"></a>sns.barplot(x<span class="op">=</span><span class="st">&#39;Pclass&#39;</span>, y<span class="op">=</span><span class="st">&#39;Survived&#39;</span>, data<span class="op">=</span>data)</span>
<span id="cb13-2"><a href="#cb13-2" aria-hidden="true" tabindex="-1"></a>plt.title(<span class="st">&#39;Survival Rate by Passenger Class&#39;</span>)</span>
<span id="cb13-3"><a href="#cb13-3" aria-hidden="true" tabindex="-1"></a>plt.show()</span></code></pre></div>
<div class="output display_data">
<p><img
src="vertopal_02cd93c0ceb54a44986da2c869cef483/9dbecc3db5ce44ad2598eee80af7537286939f98.png" /></p>
</div>
</div>
<div id="QGk7gviy5S9H" class="cell markdown" id="QGk7gviy5S9H">
<h1 id="survival-rate-by-embarkation-port">Survival rate by embarkation
port</h1>
</div>
<div id="d0O0h3Ro5TE2" class="cell code" data-execution_count="14"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:472}"
id="d0O0h3Ro5TE2" data-outputId="c94ceb52-d8c9-4492-f5b0-ffc1088415b6">
<div class="sourceCode" id="cb14"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb14-1"><a href="#cb14-1" aria-hidden="true" tabindex="-1"></a>sns.barplot(x<span class="op">=</span><span class="st">&#39;Embarked&#39;</span>, y<span class="op">=</span><span class="st">&#39;Survived&#39;</span>, data<span class="op">=</span>data)</span>
<span id="cb14-2"><a href="#cb14-2" aria-hidden="true" tabindex="-1"></a>plt.title(<span class="st">&#39;Survival Rate by Embarkation Port&#39;</span>)</span>
<span id="cb14-3"><a href="#cb14-3" aria-hidden="true" tabindex="-1"></a>plt.show()</span></code></pre></div>
<div class="output display_data">
<p><img
src="vertopal_02cd93c0ceb54a44986da2c869cef483/a830cf82203d9996765a14167cd775c78738a3da.png" /></p>
</div>
</div>
<div id="qHLXiGMy5TKy" class="cell markdown" id="qHLXiGMy5TKy">
<h1 id="step-4-correlation-matrix">Step 4: Correlation Matrix</h1>
</div>
<div id="zpHwwhH95uZu" class="cell markdown" id="zpHwwhH95uZu">
<h1 id="compute-correlation-matrix-only-numeric-columns">Compute
correlation matrix (only numeric columns)</h1>
</div>
<div id="SNwJH2dV5TQV" class="cell code" data-execution_count="15"
id="SNwJH2dV5TQV">
<div class="sourceCode" id="cb15"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb15-1"><a href="#cb15-1" aria-hidden="true" tabindex="-1"></a>correlation_matrix <span class="op">=</span> data.select_dtypes(include<span class="op">=</span>[<span class="st">&#39;float64&#39;</span>, <span class="st">&#39;int64&#39;</span>]).corr()</span></code></pre></div>
</div>
<div id="Mez4K0rs5R1J" class="cell markdown" id="Mez4K0rs5R1J">
<h1 id="plot-heatmap">Plot heatmap</h1>
</div>
<div id="G4xq7V1c5QX4" class="cell code" data-execution_count="16"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:522}"
id="G4xq7V1c5QX4" data-outputId="2b498648-f832-4f2c-97af-abb482d20881">
<div class="sourceCode" id="cb16"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb16-1"><a href="#cb16-1" aria-hidden="true" tabindex="-1"></a>sns.heatmap(correlation_matrix, annot<span class="op">=</span><span class="va">True</span>, cmap<span class="op">=</span><span class="st">&#39;coolwarm&#39;</span>)</span>
<span id="cb16-2"><a href="#cb16-2" aria-hidden="true" tabindex="-1"></a>plt.title(<span class="st">&#39;Correlation Matrix&#39;</span>)</span>
<span id="cb16-3"><a href="#cb16-3" aria-hidden="true" tabindex="-1"></a>plt.show()</span></code></pre></div>
<div class="output display_data">
<p><img
src="vertopal_02cd93c0ceb54a44986da2c869cef483/9fb581c2c5ce350a6901356f6c9379277f1debd3.png" /></p>
</div>
</div>
<div id="955Pi8Wa6UgJ" class="cell markdown" id="955Pi8Wa6UgJ">
<h1 id="import-required-libraries">Import required libraries</h1>
</div>
<div id="Nymr2ZFI6U23" class="cell code" data-execution_count="17"
id="Nymr2ZFI6U23">
<div class="sourceCode" id="cb17"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb17-1"><a href="#cb17-1" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> sklearn.model_selection <span class="im">import</span> train_test_split</span>
<span id="cb17-2"><a href="#cb17-2" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> sklearn.linear_model <span class="im">import</span> LogisticRegression</span>
<span id="cb17-3"><a href="#cb17-3" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> sklearn.metrics <span class="im">import</span> accuracy_score, classification_report, confusion_matrix</span></code></pre></div>
</div>
<div id="MSCdu3Po6U9S" class="cell markdown" id="MSCdu3Po6U9S">
<h1 id="prepare-data-for-model">Prepare data for model</h1>
</div>
<div id="m41LsKi26VF5" class="cell code" data-execution_count="18"
id="m41LsKi26VF5">
<div class="sourceCode" id="cb18"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb18-1"><a href="#cb18-1" aria-hidden="true" tabindex="-1"></a>data[<span class="st">&#39;Sex&#39;</span>] <span class="op">=</span> data[<span class="st">&#39;Sex&#39;</span>].<span class="bu">map</span>({<span class="st">&#39;male&#39;</span>: <span class="dv">0</span>, <span class="st">&#39;female&#39;</span>: <span class="dv">1</span>})  <span class="co"># Encode &#39;Sex&#39; column</span></span>
<span id="cb18-2"><a href="#cb18-2" aria-hidden="true" tabindex="-1"></a>data[<span class="st">&#39;Embarked&#39;</span>] <span class="op">=</span> data[<span class="st">&#39;Embarked&#39;</span>].<span class="bu">map</span>({<span class="st">&#39;C&#39;</span>: <span class="dv">0</span>, <span class="st">&#39;Q&#39;</span>: <span class="dv">1</span>, <span class="st">&#39;S&#39;</span>: <span class="dv">2</span>})  <span class="co"># Encode &#39;Embarked&#39; column</span></span>
<span id="cb18-3"><a href="#cb18-3" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb18-4"><a href="#cb18-4" aria-hidden="true" tabindex="-1"></a>X <span class="op">=</span> data[[<span class="st">&#39;Pclass&#39;</span>, <span class="st">&#39;Sex&#39;</span>, <span class="st">&#39;Age&#39;</span>, <span class="st">&#39;SibSp&#39;</span>, <span class="st">&#39;Parch&#39;</span>, <span class="st">&#39;Fare&#39;</span>, <span class="st">&#39;Embarked&#39;</span>]]</span>
<span id="cb18-5"><a href="#cb18-5" aria-hidden="true" tabindex="-1"></a>y <span class="op">=</span> data[<span class="st">&#39;Survived&#39;</span>]</span></code></pre></div>
</div>
<div id="oGNeel_P6VNG" class="cell markdown" id="oGNeel_P6VNG">
<h1 id="split-data-into-train-and-test-sets">Split data into train and
test sets</h1>
</div>
<div id="ZV48JqvF6VT-" class="cell code" data-execution_count="19"
id="ZV48JqvF6VT-">
<div class="sourceCode" id="cb19"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb19-1"><a href="#cb19-1" aria-hidden="true" tabindex="-1"></a>X_train, X_test, y_train, y_test <span class="op">=</span> train_test_split(X, y, test_size<span class="op">=</span><span class="fl">0.2</span>, random_state<span class="op">=</span><span class="dv">42</span>)</span></code></pre></div>
</div>
<div id="jnXXy5uT6h6H" class="cell markdown" id="jnXXy5uT6h6H">
<h1 id="train-logistic-regression-model">Train logistic regression
model</h1>
</div>
<div id="YOZdqTt46jIu" class="cell code" data-execution_count="20"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;,&quot;height&quot;:223}"
id="YOZdqTt46jIu" data-outputId="8a38db70-0417-47cc-f7a2-7e21a664bb77">
<div class="sourceCode" id="cb20"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb20-1"><a href="#cb20-1" aria-hidden="true" tabindex="-1"></a>model <span class="op">=</span> LogisticRegression()</span>
<span id="cb20-2"><a href="#cb20-2" aria-hidden="true" tabindex="-1"></a>model.fit(X_train, y_train)</span></code></pre></div>
<div class="output stream stderr">
<pre><code>/usr/local/lib/python3.10/dist-packages/sklearn/linear_model/_logistic.py:469: ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

Increase the number of iterations (max_iter) or scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
  n_iter_i = _check_optimize_result(
</code></pre>
</div>
<div class="output execute_result" data-execution_count="20">
<style>#sk-container-id-1 {
  /* Definition of color scheme common for light and dark mode */
  --sklearn-color-text: black;
  --sklearn-color-line: gray;
  /* Definition of color scheme for unfitted estimators */
  --sklearn-color-unfitted-level-0: #fff5e6;
  --sklearn-color-unfitted-level-1: #f6e4d2;
  --sklearn-color-unfitted-level-2: #ffe0b3;
  --sklearn-color-unfitted-level-3: chocolate;
  /* Definition of color scheme for fitted estimators */
  --sklearn-color-fitted-level-0: #f0f8ff;
  --sklearn-color-fitted-level-1: #d4ebff;
  --sklearn-color-fitted-level-2: #b3dbfd;
  --sklearn-color-fitted-level-3: cornflowerblue;

  /* Specific color for light theme */
  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));
  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-icon: #696969;

  @media (prefers-color-scheme: dark) {
    /* Redefinition of color scheme for dark theme */
    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));
    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-icon: #878787;
  }
}

#sk-container-id-1 {
  color: var(--sklearn-color-text);
}

#sk-container-id-1 pre {
  padding: 0;
}

#sk-container-id-1 input.sk-hidden--visually {
  border: 0;
  clip: rect(1px 1px 1px 1px);
  clip: rect(1px, 1px, 1px, 1px);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}

#sk-container-id-1 div.sk-dashed-wrapped {
  border: 1px dashed var(--sklearn-color-line);
  margin: 0 0.4em 0.5em 0.4em;
  box-sizing: border-box;
  padding-bottom: 0.4em;
  background-color: var(--sklearn-color-background);
}

#sk-container-id-1 div.sk-container {
  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`
     but bootstrap.min.css set `[hidden] { display: none !important; }`
     so we also need the `!important` here to be able to override the
     default hidden behavior on the sphinx rendered scikit-learn.org.
     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */
  display: inline-block !important;
  position: relative;
}

#sk-container-id-1 div.sk-text-repr-fallback {
  display: none;
}

div.sk-parallel-item,
div.sk-serial,
div.sk-item {
  /* draw centered vertical line to link estimators */
  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));
  background-size: 2px 100%;
  background-repeat: no-repeat;
  background-position: center center;
}

/* Parallel-specific style estimator block */

#sk-container-id-1 div.sk-parallel-item::after {
  content: "";
  width: 100%;
  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);
  flex-grow: 1;
}

#sk-container-id-1 div.sk-parallel {
  display: flex;
  align-items: stretch;
  justify-content: center;
  background-color: var(--sklearn-color-background);
  position: relative;
}

#sk-container-id-1 div.sk-parallel-item {
  display: flex;
  flex-direction: column;
}

#sk-container-id-1 div.sk-parallel-item:first-child::after {
  align-self: flex-end;
  width: 50%;
}

#sk-container-id-1 div.sk-parallel-item:last-child::after {
  align-self: flex-start;
  width: 50%;
}

#sk-container-id-1 div.sk-parallel-item:only-child::after {
  width: 0;
}

/* Serial-specific style estimator block */

#sk-container-id-1 div.sk-serial {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--sklearn-color-background);
  padding-right: 1em;
  padding-left: 1em;
}


/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is
clickable and can be expanded/collapsed.
- Pipeline and ColumnTransformer use this feature and define the default style
- Estimators will overwrite some part of the style using the `sk-estimator` class
*/

/* Pipeline and ColumnTransformer style (default) */

#sk-container-id-1 div.sk-toggleable {
  /* Default theme specific background. It is overwritten whether we have a
  specific estimator or a Pipeline/ColumnTransformer */
  background-color: var(--sklearn-color-background);
}

/* Toggleable label */
#sk-container-id-1 label.sk-toggleable__label {
  cursor: pointer;
  display: block;
  width: 100%;
  margin-bottom: 0;
  padding: 0.5em;
  box-sizing: border-box;
  text-align: center;
}

#sk-container-id-1 label.sk-toggleable__label-arrow:before {
  /* Arrow on the left of the label */
  content: "▸";
  float: left;
  margin-right: 0.25em;
  color: var(--sklearn-color-icon);
}

#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {
  color: var(--sklearn-color-text);
}

/* Toggleable content - dropdown */

#sk-container-id-1 div.sk-toggleable__content {
  max-height: 0;
  max-width: 0;
  overflow: hidden;
  text-align: left;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content pre {
  margin: 0.2em;
  border-radius: 0.25em;
  color: var(--sklearn-color-text);
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content.fitted pre {
  /* unfitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {
  /* Expand drop-down */
  max-height: 200px;
  max-width: 100%;
  overflow: auto;
}

#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {
  content: "▾";
}

/* Pipeline/ColumnTransformer-specific style */

#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator-specific style */

/* Colorize estimator box */
#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

#sk-container-id-1 div.sk-label label.sk-toggleable__label,
#sk-container-id-1 div.sk-label label {
  /* The background is the default theme color */
  color: var(--sklearn-color-text-on-default-background);
}

/* On hover, darken the color of the background */
#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

/* Label box, darken color on hover, fitted */
#sk-container-id-1 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator label */

#sk-container-id-1 div.sk-label label {
  font-family: monospace;
  font-weight: bold;
  display: inline-block;
  line-height: 1.2em;
}

#sk-container-id-1 div.sk-label-container {
  text-align: center;
}

/* Estimator-specific */
#sk-container-id-1 div.sk-estimator {
  font-family: monospace;
  border: 1px dotted var(--sklearn-color-border-box);
  border-radius: 0.25em;
  box-sizing: border-box;
  margin-bottom: 0.5em;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-estimator.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

/* on hover */
#sk-container-id-1 div.sk-estimator:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-estimator.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Specification for estimator info (e.g. "i" and "?") */

/* Common style for "i" and "?" */

.sk-estimator-doc-link,
a:link.sk-estimator-doc-link,
a:visited.sk-estimator-doc-link {
  float: right;
  font-size: smaller;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1em;
  height: 1em;
  width: 1em;
  text-decoration: none !important;
  margin-left: 1ex;
  /* unfitted */
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
  color: var(--sklearn-color-unfitted-level-1);
}

.sk-estimator-doc-link.fitted,
a:link.sk-estimator-doc-link.fitted,
a:visited.sk-estimator-doc-link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
div.sk-estimator:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover,
div.sk-label-container:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover,
div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

/* Span, style for the box shown on hovering the info icon */
.sk-estimator-doc-link span {
  display: none;
  z-index: 9999;
  position: relative;
  font-weight: normal;
  right: .2ex;
  padding: .5ex;
  margin: .5ex;
  width: min-content;
  min-width: 20ex;
  max-width: 50ex;
  color: var(--sklearn-color-text);
  box-shadow: 2pt 2pt 4pt #999;
  /* unfitted */
  background: var(--sklearn-color-unfitted-level-0);
  border: .5pt solid var(--sklearn-color-unfitted-level-3);
}

.sk-estimator-doc-link.fitted span {
  /* fitted */
  background: var(--sklearn-color-fitted-level-0);
  border: var(--sklearn-color-fitted-level-3);
}

.sk-estimator-doc-link:hover span {
  display: block;
}

/* "?"-specific style due to the `<a>` HTML tag */

#sk-container-id-1 a.estimator_doc_link {
  float: right;
  font-size: 1rem;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1rem;
  height: 1rem;
  width: 1rem;
  text-decoration: none;
  /* unfitted */
  color: var(--sklearn-color-unfitted-level-1);
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
}

#sk-container-id-1 a.estimator_doc_link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
#sk-container-id-1 a.estimator_doc_link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

#sk-container-id-1 a.estimator_doc_link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
}
</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>LogisticRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label fitted sk-toggleable__label-arrow fitted">&nbsp;&nbsp;LogisticRegression<a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.5/modules/generated/sklearn.linear_model.LogisticRegression.html">?<span>Documentation for LogisticRegression</span></a><span class="sk-estimator-doc-link fitted">i<span>Fitted</span></span></label><div class="sk-toggleable__content fitted"><pre>LogisticRegression()</pre></div> </div></div></div></div>
</div>
</div>
<div id="zr6_Ujl56iw4" class="cell markdown" id="zr6_Ujl56iw4">
<h1 id="make-predictions">Make predictions</h1>
</div>
<div id="EiQbLNVz6he-" class="cell code" data-execution_count="21"
id="EiQbLNVz6he-">
<div class="sourceCode" id="cb22"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb22-1"><a href="#cb22-1" aria-hidden="true" tabindex="-1"></a>y_pred <span class="op">=</span> model.predict(X_test)</span></code></pre></div>
</div>
<div id="Pcqjb8R_6wCZ" class="cell markdown" id="Pcqjb8R_6wCZ">
<h1 id="evaluate-the-model">Evaluate the model</h1>
</div>
<div id="z2aL5uOP6wRc" class="cell code" data-execution_count="22"
data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}"
id="z2aL5uOP6wRc" data-outputId="d9a7391d-ca0b-4b21-8477-92fb3b0a400a">
<div class="sourceCode" id="cb23"><pre
class="sourceCode python"><code class="sourceCode python"><span id="cb23-1"><a href="#cb23-1" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(<span class="st">&quot;Accuracy:&quot;</span>, accuracy_score(y_test, y_pred))</span>
<span id="cb23-2"><a href="#cb23-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(<span class="st">&quot;</span><span class="ch">\n</span><span class="st">Classification Report:</span><span class="ch">\n</span><span class="st">&quot;</span>, classification_report(y_test, y_pred))</span>
<span id="cb23-3"><a href="#cb23-3" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(<span class="st">&quot;</span><span class="ch">\n</span><span class="st">Confusion Matrix:</span><span class="ch">\n</span><span class="st">&quot;</span>, confusion_matrix(y_test, y_pred))</span></code></pre></div>
<div class="output stream stdout">
<pre><code>Accuracy: 0.8100558659217877

Classification Report:
               precision    recall  f1-score   support

           0       0.83      0.86      0.84       105
           1       0.79      0.74      0.76        74

    accuracy                           0.81       179
   macro avg       0.81      0.80      0.80       179
weighted avg       0.81      0.81      0.81       179


Confusion Matrix:
 [[90 15]
 [19 55]]
</code></pre>
</div>
</div>
</body>
</html>



