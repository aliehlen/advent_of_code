setwd(dirname(parent.frame(2)$ofile))
library(data.table)
data <- "../data/day01.csv"

# read in data
fuel <- fread(data, col.names = "mass")

# part 1: fuel needed for initial mass
fuel[,fuel_needed := floor(mass/3)-2]

print(paste0("result: ", fuel[,sum(fuel_needed)]))

# part 2: account for mass of fuel
get_fuel_req <- function(mass) {
    mass_reduced <- floor(mass/3) - 2
    if (mass_reduced > 0) {
        return(mass_reduced + get_fuel_req(mass_reduced))
    } else {
        return(0)
    }
}

fuel[,fuel_needed_all := sapply(mass, FUN = get_fuel_req)]

print(paste0("result: ", fuel[,sum(fuel_needed_all)]))
