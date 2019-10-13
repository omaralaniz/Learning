# XML Basics

> Resources: 
>
> [XML External Entities](https://www.youtube.com/watch?v=gjm6VHZa_8s&t=201s) (Video)

## What is XML?

E**X**tensible  **M**arkup **L**anguage

Just like HTML, which represents the representation the content of a page, rather, XML represents the content that will be transported or even possibly stored.  XML is being used everywhere like API's, UI Layouts & Styles, Configs, and RSS. 

Let's start off with a quick look at XML code:

```xml
<?xml version="1.0"?>
<Person>
    <Name>Santiago</Name>
	<Age>56</Age>
</Person>
```

The first line describes the meta data which shows the browser which version of XML is being presented -- not always necessary. The second line,`<Person>` -- is the **root element**, it is good practice to have one have one root tag. Both the `<Name>` and the `<Age>` tags are the **children elements**. 

RULE #1 tags are case sensitive, the open tag and closing tag must match! 

RULE #2 characters such as...: `<> ""` are illegal buuut there is a way around that...

Let's Dive In:

## Entities 

You can describe this as variables from programming languages. Entities allow the user to assign a value so it can be used anywhere within the document, when declaring these entities you define them on the top in a different portion of the document called.... Document Type Definition (aka DTD).

### EXAMPLE  ONE

```xml-dtd
<?xml version="1.0"?>
<!DOCTYPE Person [
	<!ENTITY name "Santiago">
]
<Person>
    <Name>&name;</Name>
	<Age>56</Age>
</Person>
```

If you see the example above <!ENTITY name "Santiago"> is located between two brackets, this is the DTD, `name` is the name of the entity. To use the entity in the tags yo must prefix it with an `&` and finish of with `;`.  

There three types of entitles:

#### General 

In the above example we saw the usage of the **general** entity.

#### Parameter 

Only allowed with the DTD, but it is flexible. You can set the value of an entity another ENTITY is not that grand?

```xml-dtd
<!ENTITY % outer "<!ENTITY name "Santiago">">
```



This comes in handy when doing XXE attacks

#### Predefined 

A set of entities that come predefined with the values of special characters, such as:

```xml
<hello>&#x3C;</hello>
```

`#x3C` comes with the predefined value `<` because of Rule #2's existence; `#x3C` allows us to write `<` into the XML file.

Rule #2: XML does not allow direct `<`