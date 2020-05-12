### This snippet uses Julien Piccini's Adobe Analytics 2 Python Wrapper
https://github.com/pitchmuc/adobe_analytics_api_2.0 
<p>Make sure to read all the documentation in the repository and in his blog. You need it to establish a connection with Adobe's 2.0 APIs</p>
<p>Run:</p>
<code>emoji_segments('🛒', 'your_rsid', 'Users with more than ', prefix = 1)</code>
<p>to add the emoji 🛒 at the beginning of the name to all your segments in the 'your_rsid' report suite that contains the string 'Users with more than '</p>
<p><b>Panich Mode?</b> Run:</p>
<code>remove_emojis('🛒', 'your_rsid', 'Users with more than ')</code>
<p>to remove any instance of the emoji 🛒 to all your segments in the 'your_rsid' report suite that contains the string 'Users with more than '</p>
