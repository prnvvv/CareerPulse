from nupy import algebra


def intermediate_value(function, variable, intervals, tolerance, limit):
    iterations = []
    fa_1 = intervals[0]
    fb = intervals[1]
    pn_1 = sum(intervals) / 2
    condition = algebra.evaluate(function=function, variable=variable, value=fa_1) \
                * algebra.evaluate(function=function, variable=variable, value=fb)
    if condition < 0:
        iteration_1 = 1
        while True:
            if iteration_1 == 1:
                fn_1 = algebra.evaluate(function=function, variable=variable, value=pn_1)
                fx_1 = algebra.evaluate(function=function, variable=variable, value=fa_1) * fn_1

                iterations.append([iteration_1, intervals[0], intervals[1], pn_1])

                if fx_1 < 0:
                    fx_1 *= -1.0
                    if fx_1 < tolerance:
                        break
                    else:
                        fb = pn_1
                else:
                    if fx_1 < tolerance:
                        break
                    else:
                        fa_1 = pn_1
                iteration_1 += 1

            else:
                pn_1 = (fa_1 + fb) / 2
                fn_1 = algebra.evaluate(function=function, variable=variable, value=pn_1)
                fx_1 = algebra.evaluate(function=function, variable=variable, value=fa_1) * fn_1

                iterations.append(
                    [fa_1, fb, ((fa_1 + fb) / 2), algebra.evaluate(function=function, variable=variable, value=pn_1)])
                if fx_1 < 0:
                    fx_1 *= -1.0
                    if fx_1 < tolerance:
                        break
                    else:
                        fb = pn_1
                else:
                    if fx_1 < tolerance:
                        break
                    else:
                        fa_1 = pn_1
                iteration_1 += 1

            if limit > 0:
                if iteration_1 > limit:
                    break
                elif iteration_1 > 250:
                    break
            elif iteration_1 > 250:
                break
    return iterations

