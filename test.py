import unittest
import matrix_inv


class TestHelperFuncs(unittest.TestCase):
    def test_add(self):
        ones = [[1 for j in range(4)] for i in range(4)]
        ones_inv = [[-1 for j in range(4)] for i in range(4)]
        zeros = [[0 for j in range(4)] for i in range(4)]
        matadd = matrix_inv.add_square(ones, ones_inv)

        self.assertEqual(matadd, zeros)

    def test_transpose(self):
        upper = [[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1]]
        lower = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]]
        mattranspose = matrix_inv.transpose_square(lower)

        self.assertEqual(mattranspose, upper)

    def test_dot_prod(self):
        ones = [1, -1, 1, -1]
        ones_inv = [1, 1.5, 2, 2.5]
        dp = matrix_inv.dot_prod(ones, ones_inv)

        self.assertEqual(dp, -1.0)

    def test_mult(self):
        a = [[5, 2, 6, 1], [0, 6, 2, 0], [3, 8, 1, 4], [1, 8, 5, 6]]
        b = [[7, 5, 8, 0], [1, 8, 2, 6], [9, 4, 3, 8], [5, 3, 7, 9]]
        c = [[96, 68, 69, 69], [24, 56, 18, 52], [58, 95, 71, 92], [90, 107, 81, 142]]
        ab = matrix_inv.mult_square(a, b)

        self.assertEqual(ab, c)

    def test_ident(self):
        a = matrix_inv.ident(4)
        aa = matrix_inv.mult_square(a, a)

        self.assertEqual(aa, a)


class TestMatInv(unittest.TestCase):
    def test_submat(self):
        a = [[1, 1, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
        b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        c = matrix_inv.submtrx(a, 0, 1)

        self.assertEqual(c, b)

    def test_det1(self):
        a = [[5, 2, 6, 1], [0, 6, 2, 0], [3, 8, 1, 4], [1, 8, 5, 6]]
        d = matrix_inv.det(a)

        self.assertEqual(d, -976)

    def test_det2(self):
        a = [[-5, -2, -6, -1], [0, 6, 2, 0], [3, 8, 1, 4], [1, 8, 5, 6]]
        d = matrix_inv.det(a)

        self.assertEqual(d, 976)

    def test_det3(self):
        a = [[5, 2, 6, 1], [0, 6, 2, 0], [0, 0, 0, 0], [1, 8, 5, 6]]
        d = matrix_inv.det(a)

        self.assertEqual(d, 0)

    def test_det4(self):
        a = matrix_inv.ident(4)
        d = matrix_inv.det(a)

        self.assertEqual(d, 1)

    def test_inv1(self):
        a = [[1, 1, 1, 1], [1, 1, -1, -1], [1, -1, -1, 1], [1, -1, 1, -1]]
        b = matrix_inv.inv(a)
        c = matrix_inv.mult_square(a, b)
        d = matrix_inv.ident(4)

        self.assertEqual(c, d)

    def test_inv2(self):
        a = [[2, 2, 0, 2], [4, 0, -4, -4], [0, -8, -8, 8], [16, -16, 16, -0]]
        b = matrix_inv.inv(a)
        c = matrix_inv.mult_square(a, b)
        d = matrix_inv.ident(4)

        self.assertEqual(c, d)

    def test_inv3(self):
        a = matrix_inv.ident(4)
        b = matrix_inv.inv(a)

        self.assertEqual(a, b)

    def test_inv4(self):
        a = [[1, 2, 1, 1], [1, 1, -1, -2], [1, -1, -1, 2], [1, -2, 1, -1]]
        b = matrix_inv.inv(a)
        c = [
            [0.25, 0.25, 0.25, 0.25],
            [0.2, 0.1, -0.1, -0.2],
            [0.25, -0.25, -0.25, 0.25],
            [0.1, -0.2, 0.2, -0.1],
        ]

        self.assertEqual(b, c)


if __name__ == "__main__":
    unittest.main()
