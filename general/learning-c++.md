---
description: A documentation of my learning journey of C++
---

# Learning C++

I have decided, during this period of lockdown due to COVID-19, to learn some C++. Being a maths graduate, I usually tampered with high-end languages and didn't go any lower than something like PHP. This is a shame, since learning middle or lower level languages can improve understanding of lower level concepts that are important, such as memory allocation. C++ is a middle level language and a good place for me to start.

{% hint style="info" %}
This is not a tutorial for C++ but simply an account of my learning. I used the tutorial from Tutorialspoint available [here](https://www.tutorialspoint.com/cplusplus/) to learn C++ and what is written here, either comes from, or is motivated by, this tutorial.
{% endhint %}

### Basic Notions

There are some important things to clear up before I start writing my first C++ program. Here are the distinctions between Objects, Classes, Methods and Instance Variables.

* **Object** − Objects have states and behaviors. Example: A dog has states - color, name, breed as well as behaviors - wagging, barking, eating. An object is an instance of a class.
* **Class** − A class can be defined as a template/blueprint that describes the behaviors/states that object of its type support.
* **Methods** − A method is basically a behavior. A class can contain many methods. It is in methods where the logics are written, data is manipulated and all the actions are executed.
* **Instance Variables** − Each object has its unique set of instance variables. An object's state is created by the values assigned to these instance variables.

### Hello World

As always, my first C++ program is just Hello World.

```cpp
#include <iostream>

using namespace std;

// Begin program execution
int main() {
    cout << "Hello World";

    return 0;
}
```

The main things to notice are that C++ uses a `;` to terminate statements, it encloses function code in `{}` which represent blocks and it requires declaring a variable type at the time of variable declaration.

{% hint style="warning" %}
C++ is case sensitive and identifiers \(of variables, functions etc.\) must start with a letter or an underscore and can contain any number of subsequent letters, underscores or numbers. Like other languages, C++ has some reserved keywords that cannot be used as names, these can be found [here](https://www.tutorialspoint.com/cplusplus/cpp_basic_syntax.htm).
{% endhint %}

### Data Types

C++ contains a number of primitive data types that are as follows:

| Type | Keyword |
| :---: | :---: |
| Boolean | bool |
| Character | char |
| Integer | int |
| Floating Point | float |
| Double Floating Point | double |
| Valueless | void |
| Wide Character | wchar\_t |

These primitive data types can be modified using the prefixes signed, unsigned, short or long to make other data types. These do as they say, unsigned makes a number non-negative and long/short changes the length of a number.

The size of a data type can be determined using the `sizeof()` function applied to a data type.

#### Creating New Data Types

New data types can be created using `typedef type name`. For example, to define a new type called whale we can use the following code:

```cpp
typedef string whale;
whale Betty "My name is Betty and I am a whale";
```

Which defines a whale named Betty with the given string value.

Enumeration data types can also be created using the `enum` keyword:

```cpp
enum whale {small, medium, large = 3} w;
w = medium;
```

Here the value of the first name is 0, the second 1, etc. Though we can assign specific values to a name, like we have with `large = 3`.

### Variable Types

The basic variable types are, unsuprisingy, the same as those for the data types. We define variables by indicating their type followed by their name. Multiple variables can be instantiated at the same time and a value may or may not be asigned. For example:

```cpp
int a = 3;
float a,b,c;
char z, x = 'x';

```

Where variables are defined without an initial value, they take the value NULL with all bytes set to 0.

We have two kinds of expressions in C++, lvalues and rvalues. **lvalues** are expressions that refer to a memory location and can appear either on **the left or right of an assignment**. **rvalues** on the other hand refer to data values that are stored in some address in memory and can appear **only to the right of an assignment**, since they cannot be assigned a value.

### Variable Scope

The scope of a variable is the region of the program where that variable exists. Variables can be declared within a function, in which case it is a local variable. Alternatively, if it is declared outside of a function it is called a global variable. If it is declared in the definition of a function, then it is called a formal parameter.

When a local variable is definied it is not initialised by the system and so it must be initialised by the author. Global variables are initialised to their default values, however it is good to initialise variables properly to avoid unexpected results.

For more information regarding local and global variables, visit [here](https://www.tutorialspoint.com/cplusplus/cpp_variable_scope.htm).

### Constants/Literals

Constants are fixed values that the program may not alter. They are called literals, they _literally_ are their assigned value.

{% tabs %}
{% tab title="Integers" %}
An integer literal can be a decimal, octal or hexidecimal constant. Prefixes specify the base of the constant: 0x for Hexidecimal, 0 for octal and nothing for decimal. A suffix that is a combination of U and L can be used to declare that the constant is unsigned and/or long. These suffixes can be uppercase or lowercase and in any order. For example:

```cpp
10 \\ Legal
0xFeeL \\ Legal
078 \\ Illegal, 8 is not an octal digit
37uu \\ Illegal, since suffixes cannot be repeated
```
{% endtab %}

{% tab title="Floating Points" %}
A floating point literal has an integer part, a decimal point, a fractional oart and an exponent part. To use decimal form, the decimal point or exponent must be included. For Example:

```cpp
3.1415926535 \\ Legal
3.14e-5 \\ Legal
.e1 \\ Illegal, no integer or fractional part
5e \\ Illegal, no exponent given

```
{% endtab %}

{% tab title="Booleans" %}
Booleans take two values: `true` or `false`. That's it!
{% endtab %}

{% tab title="Characters" %}
Character literals are enlcosed in **single** quotes. If it begins with L then it is a wide character literal and should be stored in the **wchar\_t** variable type. Otherwise it is stored in the normal **char** type.

\ is used as an escape sequence and allows to represent specific characters, some popular ones are:

| Escape Sequence | Meaning |
| :---: | :---: |
| \n | New Line |
| \t | Horizontal Tab |
| \v | Vetical Tab |
| \r | Return |
| \b | Backspace |
| \' or \" or \\ or \? | Escaped Character |
{% endtab %}

{% tab title="Strings" %}
String literals are enclosed in **double** quotes, distinguishing them from characters. A string is made up of characters and includes the escape sequences that characters use. For example:

```cpp
"h" \\ String containing the character h
"Hello World"
"Hello \
World" \\ Represents same string as above
"Hell" "o" " World" \\ Also the same string
```
{% endtab %}
{% endtabs %}

Constants can be defined in two ways, using the const variable type or the \#define preprocessor. It is good practice to use all capitals for constant variables.

```cpp
#define LENGTH 10;
const int LENGTH = 10;
```

### Storage Classes

A storage class defines the scope and life-time of variables and functions. The storage class precedes the type that they modify.

{% tabs %}
{% tab title="auto" %}
This is the default storage class for all local variables and it can only be used to define local variables i.e within functions. Therefore `int x` is the same as `auto int x` when used inside a function.
{% endtab %}

{% tab title="register" %}
The register storage class is used to define local variables that should be stored in a register instead of RAM. Therefore, the variable size has a maximum size that is equal to the register size \(usually one word\) and it cannot have the unary operator '&'.

This should only be used for variables that require quick access such as counters for a loop.

{% hint style="warning" %}
Defining the storage class as register does not mean that the variable will be stored in a register, but that it might be, if hardware implentation allows it.
{% endhint %}
{% endtab %}

{% tab title="static" %}
The **static** storage class instructs the compiler to keep a local variable in existence during the life-time of the program instead of creating and destroying it each time it comes into and goes out of scope. Therefore, making local variables static allows them to maintain their values between function calls.

The static modifier may also be applied to global variables. When this is done, it causes that variable's scope to be restricted to the file in which it is declared.

In C++, when static is used on a class data member, it causes only one copy of that member to be shared by all objects of its class.
{% endtab %}

{% tab title="extern" %}
The **extern** storage class is used to give a reference of a global variable that is visible to ALL the program files. When you use 'extern' the variable cannot be initialized as all it does is point the variable name at a storage location that has been previously defined.

When you have multiple files and you define a global variable or function, which will be used in other files also, then extern will be used in another file to give reference of defined variable or function. Just for understanding extern is used to declare a global variable or function in another file.

The extern modifier is most commonly used when there are two or more files sharing the same global variables or functions.
{% endtab %}

{% tab title="mutable" %}
The **mutable** specifier applies only to class objects. It allows a member of an object to override const member function. That is, a mutable member can be modified by a const member function.
{% endtab %}
{% endtabs %}

### Operators

Operators are symbols that tell the compiler to do specific actions. They are built in, fundamental functions. Arithmetic and Relational Operators are the same as in \(almost\) every other language, here are some operators that may differ:

{% tabs %}
{% tab title="Logical" %}
| Operator | Description |
| :--- | :--- |
| && | Logical AND |
| \|\| | Logical OR |
| ! | Logical NOT |
{% endtab %}

{% tab title="Bitwise" %}
Bitwise operators work on bits, performing bitwise operations.

Let A = 0011 1100 and B = 0000 1101.

| Operator | Description | Example |
| :--- | :--- | :--- |
| & | Binary AND | A&B = 0000 1100 |
| \| | Binary OR | A\|B = 0011 1101 |
| ^ | Binary XOR | A ^ B = 0011 0001 |
| ~ | Binary Complement | ~A = 1100 0011 |
| &lt;&lt; | Binary Left Shift | A &lt;&lt; 2 = 1111 0000 |
| &gt;&gt; | Binary Right Shift | A &gt;&gt; 2 = 0000 1111 |
{% endtab %}

{% tab title="Misc" %}
There are a number of miscallaneous operators that are supported by C++

| Operator | Description |
| :--- | :--- |
| sizeof | Returns the size of a variable |
| Condition ? X : Y | If condition is true, return X, else Y |
| , | This causes a sequence of operations to be performed, the value is the last expression in the comma seperated list. |
| . and -&gt; | Member operators |
| Cast | convert one data type to another |
| & | returns the address of a variable in memory. |
| \* | A pointer to a variable, for exmple \*var will point to the variable var |
{% endtab %}
{% endtabs %}

For information regarding operator preference, please see [here](https://www.tutorialspoint.com/cplusplus/cpp_operators.htm).

### Loops

C++ supports the usual loops. The syntax for implentation is below.

#### While Loop

```cpp
while(condition) {
    statement(s);
}
```

#### For Loop

Below is the implentation of the for loop. The `init` condition is executed first and then the `condition` is evaluated. After the body of the loop is executed, the `increment` statement is executed and the condition is evaluated again. This cycle between incrementation and condition evaluation continues until the condition is evaluated as false, whence the loop terminates.

```cpp
for ( init; condition; increment) {
    statement(s);
}
```

