library(data.table)

data_file <- "../data/day1.txt" 
data <- fread(data_file)

# part 1 - product of 2 numbers whose sum is 2020

combos2 <- data.table(t(combn(data[[1]], 2)))
combos2[,sum := V1 + V2]
ans = combos2[sum == 2020, .(V1, V2, prod = V1*V2)]

print(paste("the values are", ans[,V1], "and", ans[,V2], 
            "and the product is", ans[,prod]))

# part 2 - product of 3 numbers whose sum is 2020

combos3 <- data.table(t(combn(data[[1]], 3)))
combos3[,sum := V1 + V2 + V3]
ans = combos3[sum == 2020, .(V1, V2, V3, prod = V1*V2*V3)]

print(paste("the values are", ans[,V1], "and", ans[,V2], "and", ans[,V3], 
            "and the product is", ans[,prod]))
