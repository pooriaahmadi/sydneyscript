# SydneyScript - A programming language

A toy programming language made from scratch with python based on my friend's most used words as keywords as a gift. TOTALLY NOT FOR [@sydeich](https://github.com/sydeich)

## FAQ

#### Why?

Sometimes you need to give ppl something that they deserve, right?

#### Will it get updated?

Absolutely not.

#### Can I contribute?

YESSS

## Installation

Install SydneyScript with pip:

```bash
  > pip install sydneyscript
  done!
```

Running an app:

```bash
> sydneyscript FILENAME.syd
```

SydneyScript shell:

```bash
> sydneyscript
```

## Hello world

Lets code a different hello world application!

```javascript
# hello_world.syd
FUNKY uwuify(prefix) -> prefix + " UWU"

FUNKY mass_uwu_print(text, times)
    PARADOX i = 0 TO times SOWHAT
        SHOUT(uwuify(text))
    YUMYUM
YUMYUM

mass_uwu_print("Hello world", 10)

# OUTPUT: "Hello world UWU" * 10
```

## Features

-   Variables
-   AND / OR
-   IF / ELSE IF / ELSE
-   FOR / WHILE
-   FUNCTIONS

## Syntax

| Tradtional keyword | SydneyScript keyword    |
| ------------------ | ----------------------- |
| const              | BOWL                    |
| and                | AND                     |
| or                 | OAR                     |
| not                | FLIP                    |
| if                 | DEBATE                  |
| else if            | TOLDYOU                 |
| else               | LASTCHANCE              |
| for                | PARADOX                 |
| step               | STEP                    |
| while              | SINCE                   |
| function/def       | FUNKY                   |
| then               | SOWHAT                  |
| end                | YUMYUM                  |
| return             | YEET                    |
| continue           | EVERYTHINGISGONNABEFINE |
| break              | DOOMED                  |

#### BuiltIn functions and variables

| Name               | Meaning                           |
| ------------------ | --------------------------------- |
| VOID               | null                              |
| HELLYEA            | false                             |
| HELLNO             | true                              |
| NERD_NUMBER        | PI number                         |
| SHOUT              | print                             |
| NO_INPUT           | asking for input                  |
| NO_INT             | asking for a number               |
| GETRIDOFEVERYTHING | clear the console                 |
| GROE               | clear the console                 |
| IS_NUMBER          | check if the input is a number    |
| IS_STRING          | check if the input is a string    |
| IS_BAG             | check if the input is a list      |
| IS_FUNKY           | check if the input is a function  |
| PUSH               | Add something to a list           |
| POP                | Remove the last element from list |
| STRETCH            | Adding to lists together          |
| HOWLONG            | getting the length of list        |
| UWU                | running a \*.syd script           |

#### Variables

```javascript
BOWL cool_variable = "I'm a cool string variable!"
```

#### For Loops

```javascript
PARADOX i = 0 TO 10 SOWHAT
	SHOUT(i)
YUMYUM
```

#### Functions

```javascript
FUNKY say_hello(name)
	YEET "Hello " + name
YUMYUM
# OR
FUNKY say_hello(name) -> "Hello " + name
```

#### If Statement

```javascript
DEBATE (2+2 == 5) SOWHAT
	SHOUT("2+2 is equal to 5")
TOLDYOU (2+2 == 4) SOWHAT
	SHOUT("2+2 is equal to 4")
LASTCHANCE SHOUT("WHO CARES?")
```

## Author(s)

-   [@pooriaahmadi](https://www.github.com/pooriaahmadi)

## License

[MIT](https://choosealicense.com/licenses/mit/)
