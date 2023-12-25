
class AES:

    Rcon = [
        0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
        0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
        0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
        0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    ]

    mix_columns_matrix = [
        ['02', '03', '01', '01'],
        ['01', '02', '03', '01'],
        ['01', '01', '02', '03'],
        ['03', '01', '01', '02']
    ]

    @staticmethod
    def constructMatrix(B):
        matrix = [
            [B[0], B[4], B[8], B[12]],
            [B[1], B[5], B[9], B[13]],
            [B[2], B[6], B[10], B[14]],
            [B[3], B[7], B[11], B[15]]
        ]
        return matrix
    
    @staticmethod
    def shiftRows(matrix):
        matrix[1] = matrix[1][1:] + matrix[1][0:1]
        matrix[2] = matrix[2][2:] + matrix[2][0:2]
        matrix[3] = matrix[3][3:] + matrix[3][0:3]
        return matrix

    @staticmethod
    def mixColumns(matrix):
        pass
