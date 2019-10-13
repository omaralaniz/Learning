# Application Security Basics

## What is Application?

Application encompasses three layers in the OSI model, which, is made of seven layers: Application, Presentation, Session, Transport, Network, Data Link, and Physical. 

Fail to protect MILLIONS of users at RISK!!!

## TLS

<u>T</u>ransport <u>L</u>ayer <u>S</u>ecurity and <u>S</u>ecure <u>S</u>ocket <u>L</u>ayer.

SSL is no longer supported. SO USE TLS.

TLS supports end to end encryption meaning it will stay encrypted when you send your data from your web browser all the way to the server-- and vise versa. Firstly, the server will send a certificate that the end user's web browser will have to validate, once the web browser validates the certificate and deems it worthy the browser is ready to set up the end to end encryption with the server. 

Without TLS a web browser will have just the standard HTTP security protocol, which, in reality it isn't a secure protocol at all. An evildoer at any moment interfere with the package your web browser sent that you initiated; it can not only receive the package but the evildoer can modify the package mid transportation! When using TLS allow of your content on your webpage is encrypted!!!

How to implement TLS:

Create your own certificate by using the Openssl open source project another possible way to get a certificate is by buying it usually from your sever provider.

When you create an Openssl certificate it will be considered self signed certificate and under the authority that keeps the internet safe will not validate it for that reason. SO, if you're webpage is self signed you will get a message warning the end user that the webpage is not totally secured. 

So must times people prefer to purchase the certificate from authorities such as Let's Encrypt and Cloudfare. Let's Encrypt  will encrypt your webpage using TLS and Cloudfare will use <u>C</u>ontent <u>D</u>elivery <u>N</u>etwork (CDN) , allow to configure your DNS settings that will allow encryption between the client side and the server side.



