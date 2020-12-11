<img align="right" width="175" height="175" src="https://github.com/nenb/Py-Projects/blob/main/matrix_inv/foobar.png?raw=true">

# matrix_inv

A basic Python implementation for computing the inverse of a matrix. Written during completion of [Google Foobar Challenge](https://foobar.withgoogle.com/).

## Usage

You can run matrix_inv as follows:

```sh
python __main__.py [-i] infile.csv [outfile.csv]
```

The input file `infile.csv` contains the input matrix. Each entry should be
delimited by a comma, and each row should be on a new line. For example, the
input file for the 3x3 identity matrix would be:
```
1,0,0
0,1,0
0,0,1
```

Given an input matrix, matrix_inv will compute the inverse of this matrix (if
it exists) and will output to screen. If an output file `outfile.csv` is supplied,
the inverse matrix will be saved to this file instead in a similar format as the
input file.

If the option `-i` is supplied, input will be taken from standard input.
