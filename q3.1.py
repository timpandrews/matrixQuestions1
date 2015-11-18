'''
Q3
Consider an application where invoices have multiple line items.
Line items can be either 'internal' or 'external'; a number of internal
line items can be summed up to produce either an internal or an external
line item.  The distinction 'external' means that that line item will
print on the invoice that the end user sees.

An invoice contains a list of line items, all of which must be external;
each of these line items may have internal line items. For example, the
external line item "Membership Dues" may be the sum of internal line
items for "State Dues", "National Dues", and "Administrative Fees".

Q3-1. Write a function verify_amount that takes a LineItem and verifies
that the internal line items all sum up correctly to the amount of their
parent, returning true or false.

Q3-2. On an invoice, we only display the external lines so printing is
easy. For debugging purposes, though, we want to output the whole tree
and number each line item.  Write a function print_line_item() that
formats the tree of line items, producing something
like the following:

'''

from decimal import Decimal

class LineItem:
     """
     Instance attributes:
       amount: Decimal
       _lineItems: list of child internal lineitems (possibly an empty list)
       isInternal: bool
     """

     def __init__(self, **kw):

         self.amount = Decimal(0)
         self._lineItems = []
         self.isInternal = False
         for k, v in kw.items():
             setattr(self, k, v)

def verify_amount(externalLineItem):
    internalLineItemSum = 0

    if hasattr(externalLineItem, 'lineItems'):
        # Add up amounts for all internalLineItems
        for internalLineItem in externalLineItem.lineItems:
            #print internalLineItem.amount
            internalLineItemSum += internalLineItem.amount
        #print internalLineItemSum

        # if values are equal then amounts are verified otherwise the external lineItem amount is incorrect
        if externalLineItem.amount == internalLineItemSum:
            return True
        else:
            return False
    else:
        #If ext lineItem does not have the attr lineItems then it is a standalone lineitem and the amount is verfified
        return True

def print_lineItem(ExternalLineItems):
    print "\n\nInvoice Tree (including both external & internal line items)"
    for lineNumber, lineItem in enumerate(ExternalLineItems):
        if hasattr(lineItem, 'lineItems'):
            for lineNumber_2ndLevel, internalLineItem in enumerate(lineItem.lineItems):
                if hasattr(internalLineItem, 'lineItems'):
                    for lineNumber_3rdLevel, ThirdLevelLineItem in enumerate(internalLineItem.lineItems):
                        print "  ", lineNumber + 1, ".", lineNumber_2ndLevel + 1, ".", lineNumber_3rdLevel + 1, ThirdLevelLineItem.description, ThirdLevelLineItem.amount
                else:
                    print "  ", lineNumber + 1, ".", lineNumber_2ndLevel + 1, internalLineItem.description, internalLineItem.amount
        else:
            print "  ", lineNumber + 1, lineItem.description, lineItem.amount



def main():

    # External line item with no children
    ext1 = LineItem(amount=Decimal(100), description='Standalone charge')

    # External line item with one level of children
    int1 = LineItem(amount=Decimal('1886.75'), description='State Dues', isInternal=True)
    int2 = LineItem(amount=Decimal('232.50'), description='National Dues', isInternal=True)
    int3 = LineItem(amount=Decimal('50'), description='Processing Fee', isInternal=True)
    ext2 = LineItem(amount=Decimal('2169.25'), description='Dues', lineItems=[int1, int2, int3])


    # Line item where one internal line item itself contains two nested items.
    int4 = LineItem(amount=Decimal('2119.25'), description='Association Dues', lineItems=[int1, int2], isInternal=True)
    ext3 = LineItem(amount=Decimal('2169.25'), description='Dues',lineItems=[int4, int3])

    # Line item where the amounts don't sum up properly.
    bad_ext = LineItem(amount=Decimal('2169.00'), description='Dues', lineItems=[int4, int3])


    # Q3.1 Verifies that the internal line items all sum up correctly to the amount of their parent
    print "External Line Item 1 Amount Verified = ", verify_amount(ext1)
    print "External Line Item 2 Amount Verified = ", verify_amount(ext2)
    print "External Line Item 3 Amount Verified = ", verify_amount(ext3)
    print "External Line Item 'bad_ext' Amount Verified = ", verify_amount(bad_ext)

    # Q3.2 Print Out of complete Invoice Tree (including both external and internal line items)
    print_lineItem([ext1, ext2, ext3])

if __name__=="__main__":
     main()
