# Returns TRUE if there are any NA's else FALSE
anynas <- function(col) {
  any(is.na(col))
}

# usage
anynas(dataframe$columnname)