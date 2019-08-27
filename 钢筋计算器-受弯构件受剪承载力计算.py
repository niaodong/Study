# -*- coding: utf-8 -*-
import math
"""
受弯构件受剪承载力计算 V0.1
默认单位N,mm
"""
print("受弯构件受剪承载力计算 V0.1\n默认单位N,mm")
V = 0
Asv1 = 0
S = 0
n = 0
Vcs = 0
Vc = 0


# 剪力V未知
def UnknowV():
    q = int(input("请输入均布荷载q："))
    l0 = int(input("请输入构件长度l0："))
    global V
    V = (q * l0) / 2
    return V


# V已知
def KnowV():
    global V
    V = float(input("请输入剪力设计值V："))
    return V


# 按计算配置箍筋
def SHoop():
    M1 = (V - Vc) / (fyv * h0)
    d = float(input("请输入所选箍筋的直径："))
    global Asv1
    Asv1 = (d ** 2 * math.pi) / 4
    global S
    S = float(input("请输入箍筋间距："))
    global n
    n = int(input("请输入几支箍："))
    M2 = (n * Asv1) / S
    # 判断箍筋面积是否满足要求
    if M2 > M1:
        print("nAsv1/S = %.4f > %.4f 可以" % (M2, M1))
    else:
        print("nAsv1/S = %.4f < %.4f 请重选箍筋" % (M2, M1))
        return SHoop()


# 按构造配置箍筋
def GHoop():
    d = int(input("请输入所选箍筋的直径："))
    global Asv1
    Asv1 = (d ** 2 * math.pi()) / 4
    n = int(input("请输入几支箍："))
    psv = 0.24 * ft / fyv
    S = (n * Asv1) / b * psv
    print("箍筋间距S=%.2f" % S)


# 配置弯起钢筋
def Bead():
    Asb = int(input("请输入弯起钢筋的面积："))
    rad = int(input("请输入纵筋弯起的角度："))
    Vsb = 0.8 * Asb * fy * math.sin((rad * math.pi) / 180)
    if Vc + Vsb > V:
        # 按构造配箍筋
        d = int(input("请输入所选箍筋的直径："))
        global Asv1
        Asv1 = (d ** 2 * math.pi) / 4
        global S
        S = float(input("请输入箍筋间距："))
        global n
        n = int(input("请输入几支箍："))
        # 判断配筋率
        psv = (n * Asv1) / (b * S)
        psvmin = 0.24 * ft / fy
        if psv > psvmin:
            print("ρsv=%.4f > ρsv·min=%.4f 可以" % (psv, psvmin))
            S = (n * Asv1) / psvmin
            print("箍筋间距S=%.2f" % S)
        else:
            print("ρsv=%.4f < ρsv·min=%.4f 请重新配置弯起钢筋和箍筋" % (psv, psvmin))
            return Bead()
    else:
        # 按计算配箍筋
        global Vcs
        Vcs = V - Vsb
        d = int(input("请输入所选箍筋的直径："))
        Asv1 = (d ** 2 * math.pi) / 4
        S = float(input("请输入箍筋间距："))
        n = int(input("请输入几支箍："))
        psv = (n * Asv1) / (b * S)
        psvmin = 0.24 * ft / fy
        # 判断配筋率
        if psv > psvmin:
            print("ρsv=%.4f > ρsv·min=%.4f 可以" % (psv, psvmin))
            S = (n * Asv1) / psvmin
            print("箍筋间距S=%.2f" % S)
        else:
            print("ρsv=%.4f < ρsv·min=%.4f 请重新配置弯起钢筋和箍筋" % (psv, psvmin))
            return Bead()
        Vcs1 = 0.7 * ft * b * h0 + (fyv * n * Asv1 * h0) / S
        # 验算混凝土+选用箍筋剪力是否大于不配置弯起钢筋时的剪力
        if Vcs1 > Vcs:
            print("V'cs=%.2f > Vcs=%.2f 可以" % (Vcs1, Vcs))
            exit()
        else:
            print("V'cs=%.2f < Vcs=%.2f 需要重新配置弯起钢筋和箍筋" % (Vcs1, Vcs))
            return Bead()


# 主程序
if __name__ == '__main__':
    # 1.输入已知
    h = int(input("请输入截面高h："))
    b = int(input("请输入界面宽b："))
    fc = float(input("请输入混凝土抗压强度fc："))
    ft = float(input("请输入混凝土抗拉强度ft："))
    fy = float(input("请输入受拉纵筋抗拉强度设计值fy："))
    fyv = float(input("请输入箍筋抗拉强度设计值fyv："))
    a1s = int(input("请输入假定as高度："))
    Bc = float(input("请输入混凝土强度影响系数βc："))
    h0 = h - a1s
    print("h0=%.2f" % h0)
    # 2.剪力设计值
    SR1 = int(input("剪力是否已知？（0：已知，1：未知）"))
    if SR1 == 0:
        KnowV()
    elif SR1 == 1:
        UnknowV()

    # 3.验算截面最小尺寸
    hw = h0
    if hw / b <= 4:
        print("厚腹梁")
        if V <= 0.25 * Bc * fc * b * h0:
            print("V=%.2f ≤ 0.25βcfcbh0 可以" % V)
        else:
            print("V=%.2f > 0.25βcfcbh0 不满足" % V)
            exit()
    elif hw / b >= 6:
        print("薄腹梁")
        if V <= 0.2 * Bc * fc * b * h0:
            print("V=%.2f ≤ 0.2βcfcbh0 可以" % V)
        else:
            print("V=%.2f > 0.2βcfcbh0 不满足" % V)
            exit()
    # 4.判断按构造配筋还是计算配筋
    # 4.1判断荷载形式
    SR2 = int(input("荷载为均布荷载还是集中荷载？（0：均布，1：集中）"))
    if SR2 == 0:
        Vc = 0.7 * ft * b * h0
    elif SR2 == 1:
        jl = float(input("请输入集中荷载距支座距离"))
        jkb = jl / h0
        Vc = 1.75 * ft * b * h0 / jkb

    # 4.2判断配筋形式
    if V < Vc:
        print("按构造配筋")
        GHoop()
    else:
        print("按计算配筋")
        # 是否配置弯起钢筋
        SR3 = int(input("是否配置弯起钢筋？（0：否，1：是）"))
        if SR3 == 0:
            SHoop()
        elif SR3 == 1:
            Bead()
