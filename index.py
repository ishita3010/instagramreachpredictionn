< !DOCTYPE
html >
< html
lang = "en" >

< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > Instagram
Reach
Prediction < / title >
< / head >

< body >
< div
style = "color:blue" >
< form
action = "{{ url_for('predict') }}"
method = "post" >
< h2 > Instagram
Reach
Prediction < / h2 >

< label
for ="likes" > Number of Likes:< / label >
< input
type = "text"
id = "likes"
name = "likes"
required >

< label
for ="saves" > Number of Saves:< / label >
< input
type = "text"
id = "saves"
name = "saves"
required >

< label
for ="comments" > Number of Comments:< / label >
< input
type = "text"
id = "comments"
name = "comments"
required >

< label
for ="shares" > Number of Shares:< / label >
< input
type = "text"
id = "shares"
name = "shares"
required >

< label
for ="profile_visits" > Number of Profile Visits:< / label >
< input
type = "text"
id = "profile_visits"
name = "profile_visits"
required >

< label
for ="follows" > Number of Follows:< / label >
< input
type = "text"
id = "follows"
name = "follows"
required >

< br > < br >
< button
type = "submit" > Predict
Reach < / button >
< / form >

< br >
< h3 > {{prediction_text}} < / h3 >
< / div >

< style >
body
{
    background - color: lightslategray;
text - align: center;
padding: 0
px;
}

form
{
    display: inline - block;
background - color: rgb(168, 131, 61);
padding: 20
px;
border - radius: 10
px;
}

input[type = "text"] {
    width: 200px;
height: 25
px;
margin: 5
px;
text - align: center;
border - radius: 5
px;
}

button
{
    padding: 10px 20px;
background - color: darkcyan;
color: white;
border: none;
< !DOCTYPE
html >
< html
lang = "en" >

       < head >
       < meta
charset = "UTF-8" >
          < meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
          < title > Instagram
Reach
Prediction < / title >
               < / head >

                   < body >
                   < div
style = "color:blue" >
        < form
action = "{{ url_for('predict') }}"
method = "post" >
         < h2 > Instagram
Reach
Prediction < / h2 >

               < label
for ="likes" > Number of Likes:< / label >
                                   < input
type = "text"
id = "likes"
name = "likes"
required >

< label
for ="saves" > Number of Saves:< / label >
                                   < input
type = "text"
id = "saves"
name = "saves"
required >

< label
for ="comments" > Number of Comments:< / label >
                                         < input
type = "text"
id = "comments"
name = "comments"
required >

< label
for ="shares" > Number of Shares:< / label >
                                     < input
type = "text"
id = "shares"
name = "shares"
required >

< label
for ="profile_visits" > Number of Profile Visits:< / label >
                                                     < input
type = "text"
id = "profile_visits"
name = "profile_visits"
required >

< label
for ="follows" > Number of Follows:< / label >
                                       < input
type = "text"
id = "follows"
name = "follows"
required >

< br > < br >
< button
type = "submit" > Predict
Reach < / button >
          < / form >

              < br >
              < h3 > {{prediction_text}} < / h3 >
                                             < / div >

                                                 < style >
                                                 body
{
    background - color: lightslategray;
text - align: center;
padding: 0
px;
}

form
{
    display: inline - block;
background - color: rgb(168, 131, 61);
padding: 20
px;
border - radius: 10
px;
}

input[type = "text"] {
    width: 200px;
height: 25
px;
margin: 5
px;
text - align: center;
border - radius: 5
px;
}

button
{
    padding: 10px 20px;
background - color: darkcyan;
color: white;
border: none;
border - radius: 5
px;
cursor: pointer;
}

h3
{
    color: black;
}
< / style >
    < / body >

        < / html >
            border - radius: 5
px;
cursor: pointer;
}

h3
{
    color: black;
}
< / style >
< / body >

< / html >
