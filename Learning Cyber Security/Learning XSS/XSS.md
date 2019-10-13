# Cross-Site Scripting (XSS)

> resource Gray Hat Hacking

## Lab 16-2: Evasion form Internet Wisdom

In this lap we are going to deal with PHP and how to get around basic XSS protections. 

`htmlspecialchars` is a function within PHP that escapes special characters

### Step 1:

Enter `asdf` for the name and `fdsa` for the address, and click register. The output should be 

```
You entered
asdf
fdsa
United States of America
```

### Step 2:

Please enter, `asdf<""=>asdf` and see what the output looks. When you hit register nothing happens but if you click `ctrl-u` to open the source code, and from there click `ctrl-f` the type `asdf` find your input. The conversion should look something like this:

```php+HTML
   <DIV class="col-sm-9">
          <INPUT type="text" id="name" name="name" placeholder=
          'asdf&lt;'&quot;()=&gt;asdf' class="form-control" autofocus="">
          <SPAN class=
          "help-block"><B>Last
          Name, First Name, eg.: Smith, John</SPAN>
   </DIV>
```

If you noticed that `< ` and `>` were changed to `&lt &gt` respectively. But if you look closely `'asdf&lt;'&quot;()=&gt;asdf'`  the only thing that survived was `'` so lets abuse that! If you look inside the `<INPUT` tag `placeholder` attribute also uses single quotes. Now, we can exploit this using events because we can no longer use HTML tags. 

The event we are going to use is `'onFocus` is used when a field is selected. For the next step, we will type in `'onFocus='alert(1)` for the name and `asdf` for the address and once you register you'll see:

```
You entered
'onFocus='alert(1)
asdf
United States of America
```

If we use `ctrl-u` you'll see that our input was not filtered so now let's add `>asdf` instead of just `asdf`.  An alert box should open! Success. Again, use `ctrl-u` and you'll see that by using a single quote it allowed us to close the `placeholder` attribute, which, allowed us to run the `onFocus` event.  Using `>asdf` allowed this exploit because the registration did not go through. In Chrome this attack is prevented. 