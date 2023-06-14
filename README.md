# Jade - General Purpose Language
## Running Code
* To go into a programming language emulator/terminal type ```go run .``` in the src/GPL folder which is the root folder. 
Here you can type any commands from the Jade language.
* To run a program file type ```go run . <file path>```.
* To see the parse tree of the code type ```go run . <file path> - t```.

## Syntax

The Jade language is somewhat similiar to C++ with some substitutions. Thus, it is not hard to learn it.

### Input/Output and Loops
```
n = int(read());

i = 0;
for ( i < n ) {
    write(i + "\n");
    i = i + 1;
}
```

### Arrays and Strings
```
name = "John";
array = [1, 5, 123, 3];

write(name, "\n");
write(array, "\n");

array = pop(array, 2);
array = push(array, 2);
write(array)
```

### Functions

```
maximum = fn(n, m) {
    if (n > m) {
        return n;
    } else {
        return m;
    }
}

write("Input the first number: ");
a = int(read());
write("Input the second number: ")
b = int(read());

max = maximum(a, b);
write("The max of the two is ",max);
```

### Control statements

```
i = 0;

if (i < 5) {
    write("True");
} else {
    write("False");
}
```

### Recursions
```
fibonacci = fn(n) {
    if (n == 0) {
        return 1;
    }

    if (n == 1) {
        return 1;
    }

    return fibonacci(n-1) + fibonacci(n-2);
}

write(fibonacci(5));
```

### Multiple functions

```
sort = fn(arr, len){

    i = 0;
    arr_new = [];
    for ( i < len){

        j = 0;
        min = arr_min(arr, len);
        for (j < len){
            if (arr[j] == min){
                arr = pop(arr, j);
                arr_new = push(arr_new, min);
                len = len - 1;
                i = -1;
            }
            j = j + 1;

        }

        i = i + 1;

    }
    return arr_new;
}


arr_min = fn(arr, len){

    i = 0;
    min = arr[0];
    for ( i < len){
        min = MIN(min, arr[i]);
        i = i + 1;
    }
    return min;  
}

MIN = fn(n, m){
    if (n < m) {
        return n;
    } else {
        return m;
    }
}

```