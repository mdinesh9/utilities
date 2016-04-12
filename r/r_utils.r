# Returns TRUE if there are any NA's else FALSE
anynas <- function(col) {
  any(is.na(col))
}

# usage
anynas(dataframe$columnname)


# -------------------------------------------------------
# Compares two datasets, and returns the missing columns in the second dataset.
missingColumn <- function(dataset1, dataset2) {
  colNames1 <- colnames(dataset1)
  colNames2 <- colnames(dataset2)
  
  colNames1[-match(colNames2, colNames1)]
}

# usage
missingColumn(train, test)