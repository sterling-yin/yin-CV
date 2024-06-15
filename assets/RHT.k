*KEYWORD
*COMMENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                       RHT MODEL PARAMETERS FOR UHPFRC                        |
|                                  kg - m - s                                  |
|        Calibrated by YIN XING, PhD - Zhejiang University (Jun, 2024)         |
|                         Contact: yinxing@zju.edu.cn                          |
| Reference                                                                    |
| Yin X, Li Q, Wang Q, Chen B, Xu S. Near range explosion resistance of UHPFRC |
| panels in wide scaled distances: Experimental study and stochastic numerical |
|     modelling. International Journal of Impact Engineering. 2024;192:105028. |
| doi: 10.1016/j.ijimpeng.2024.105028                                          |
| Note: MAT ID is 272                                                          |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*PARAMETER_EXPRESSION
$#    name expression
Rfc       120.00*(1.00-0.10)
Rfco      &fc*1E+6
Rshear    1600.00*1E+6*&fc**0.5
Rfs       1.07*2.0*2.0/&fc+0.13
Rft       0.30*&fc**(-1.0/3.0)
RQ0       0.468375+0.50625*&fc**(-1.0/3.0)
RB        0.094875-0.16875*&fc**(-1.0/3.0)
Rpel      2.0*&fco/3.0
$
*MAT_RHT_TITLE
RHT
$#     mid        ro     shear    onempa      epsf        b0        b1        t1
       272    2550.0    &shear      -1.0       0.1      1.22      1.22  35.27E+9
$#       a         n        fc       fs*       ft*        q0         b        t2
   2.27587    0.5523      &fco       &fs       &ft       &Q0        &B       0.0
$#     e0c       e0t        ec        et     betac     betat       ptf
  100000.0  100000.0   1000000   1000000       0.0       0.0     0.001
$#     gc*       gt*        xi        d1        d2       epm        af        nf
      0.99      0.80      0.01      0.01       1.0     0.007     1.676     0.735
$#   gamma        a1        a2        a3       pel       pco        np     alpha
       0.0  35.27E+9   60.0E+9   10.0E+9      &pel    6.0E+9       5.0       0.0
*END



