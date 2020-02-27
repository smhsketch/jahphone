# jahphone
Twitter for JahPhone 2

allows users to tweet from "Twitter for JahPhone 2" for comedic purposes.

to start, download the jahphone.py file. keep its path handy - we'll need it later.

let's install twurl. First, get ruby with your package manager of choice.
```
sudo apt install ruby
sudo dnf install ruby
sudo pacman -S ruby
```
then, install twurl.
```
gem install twurl
```
now that you've done that, let's configure twurl to leverage the twitter API.

add these lines to your ~/.bashrc file, replacing PATH-TO-JAHPHONE with the path to your jahphone.py file.


```
alias jahphone='python3 PATH-TO-jahphone.py'
export PATH=/home/USER/.gem/ruby/2.7.0/bin:$PATH
```
restart your terminal, then type:

```
twurl authorize --consumer-key wxZ22dtlM0yEMpdumqVblPdPN --consumer-secret 7guocd9MWxLIOWVRYeIjrTwlZDCs6liyA5KZMoDQZfm3LRnb2K
```
follow the instructions printed in the terminal - open the link in your browser, authorize the app, and paste the
authentication code into your terminal.

Once this is done, you can type the command "jahphone" into your terminal, enter a status, and your twitter account will
tweet from Twitter for JahPhone 2.
