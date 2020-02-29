# jahphone
Twitter for JahPhone 2

allows users to tweet from "Twitter for JahPhone 2" for comedic purposes.

first, download the jahphone.py file by git cloning the repo to your computer:
```
git clone https://github.com/smhsketch/jahphone.git
```

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

add these lines to your ~/.bashrc file. Replace the path with the path of your jahphone.py file if you moved it.


```
alias jahphone='python3 /home/USER/jahphone/jahphone.py'
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
