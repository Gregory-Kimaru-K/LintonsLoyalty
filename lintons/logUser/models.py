# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Loyalcustomers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customername = models.TextField(db_column='CustomerName', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    datecreated = models.DateTimeField(db_column='DateCreated', blank=True, null=True)  # Field name made lowercase.
    points = models.FloatField(db_column='Points', blank=True, null=True)  # Field name made lowercase.
    totalspend = models.FloatField(db_column='TotalSpend', blank=True, null=True)  # Field name made lowercase.
    averagebasket = models.FloatField(db_column='AverageBasket', blank=True, null=True)  # Field name made lowercase.
    checkins = models.IntegerField(db_column='CheckIns', blank=True, null=True)  # Field name made lowercase.
    redemptions = models.FloatField(db_column='Redemptions', blank=True, null=True)  # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated', blank=True, null=True)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birth_year = models.IntegerField(blank=True, null=True)
    birth_month = models.IntegerField(blank=True, null=True)
    birth_day = models.IntegerField(blank=True, null=True)
    lastseenbranch = models.CharField(db_column='LastSeenBranch', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'LoyalCustomers'

class Invnum(models.Model):
    autoindex = models.BigAutoField(db_column='AutoIndex', primary_key=True)  # Field name made lowercase.
    doctype = models.IntegerField(db_column='DocType', blank=True, null=True)  # Field name made lowercase.
    docversion = models.IntegerField(db_column='DocVersion', blank=True, null=True)  # Field name made lowercase.
    docstate = models.IntegerField(db_column='DocState', blank=True, null=True)  # Field name made lowercase.
    docflag = models.IntegerField(db_column='DocFlag', blank=True, null=True)  # Field name made lowercase.
    origdocid = models.BigIntegerField(db_column='OrigDocID', blank=True, null=True)  # Field name made lowercase.
    invnumber = models.CharField(db_column='InvNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grvnumber = models.CharField(db_column='GrvNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    grvid = models.BigIntegerField(db_column='GrvID', blank=True, null=True)  # Field name made lowercase.
    accountid = models.IntegerField(db_column='AccountID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, blank=True, null=True)  # Field name made lowercase.
    invdate = models.DateTimeField(db_column='InvDate', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateTimeField(db_column='OrderDate', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateTimeField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.
    deliverydate = models.DateTimeField(db_column='DeliveryDate', blank=True, null=True)  # Field name made lowercase.
    taxinclusive = models.BooleanField(db_column='TaxInclusive', blank=True, null=True)  # Field name made lowercase.
    email_sent = models.IntegerField(db_column='Email_Sent', blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='Address1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='Address2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address3 = models.CharField(db_column='Address3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address4 = models.CharField(db_column='Address4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address5 = models.CharField(db_column='Address5', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address6 = models.CharField(db_column='Address6', max_length=40, blank=True, null=True)  # Field name made lowercase.
    paddress1 = models.CharField(db_column='PAddress1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    paddress2 = models.CharField(db_column='PAddress2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    paddress3 = models.CharField(db_column='PAddress3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    paddress4 = models.CharField(db_column='PAddress4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    paddress5 = models.CharField(db_column='PAddress5', max_length=40, blank=True, null=True)  # Field name made lowercase.
    paddress6 = models.CharField(db_column='PAddress6', max_length=40, blank=True, null=True)  # Field name made lowercase.
    delmethodid = models.IntegerField(db_column='DelMethodID', blank=True, null=True)  # Field name made lowercase.
    docrepid = models.IntegerField(db_column='DocRepID', blank=True, null=True)  # Field name made lowercase.
    ordernum = models.CharField(db_column='OrderNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deliverynote = models.CharField(db_column='DeliveryNote', max_length=50, blank=True, null=True)  # Field name made lowercase.
    invdisc = models.FloatField(db_column='InvDisc', blank=True, null=True)  # Field name made lowercase.
    invdiscreasonid = models.IntegerField(db_column='InvDiscReasonID', blank=True, null=True)  # Field name made lowercase.
    message1 = models.CharField(db_column='Message1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    message2 = models.CharField(db_column='Message2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    message3 = models.CharField(db_column='Message3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='ProjectID', blank=True, null=True)  # Field name made lowercase.
    tillid = models.IntegerField(db_column='TillID', blank=True, null=True)  # Field name made lowercase.
    posamnttendered = models.FloatField(db_column='POSAmntTendered', blank=True, null=True)  # Field name made lowercase.
    poschange = models.FloatField(db_column='POSChange', blank=True, null=True)  # Field name made lowercase.
    grvsplitfixedcost = models.BooleanField(db_column='GrvSplitFixedCost')  # Field name made lowercase.
    grvsplitfixedamnt = models.FloatField(db_column='GrvSplitFixedAmnt', blank=True, null=True)  # Field name made lowercase.
    orderstatusid = models.IntegerField(db_column='OrderStatusID', blank=True, null=True)  # Field name made lowercase.
    orderpriorityid = models.IntegerField(db_column='OrderPriorityID', blank=True, null=True)  # Field name made lowercase.
    extordernum = models.CharField(db_column='ExtOrderNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    foreigncurrencyid = models.IntegerField(db_column='ForeignCurrencyID', blank=True, null=True)  # Field name made lowercase.
    invdiscamnt = models.FloatField(db_column='InvDiscAmnt', blank=True, null=True)  # Field name made lowercase.
    invdiscamntex = models.FloatField(db_column='InvDiscAmntEx', blank=True, null=True)  # Field name made lowercase.
    invtotexcldex = models.FloatField(db_column='InvTotExclDEx', blank=True, null=True)  # Field name made lowercase.
    invtottaxdex = models.FloatField(db_column='InvTotTaxDEx', blank=True, null=True)  # Field name made lowercase.
    invtotincldex = models.FloatField(db_column='InvTotInclDEx', blank=True, null=True)  # Field name made lowercase.
    invtotexcl = models.FloatField(db_column='InvTotExcl', blank=True, null=True)  # Field name made lowercase.
    invtottax = models.FloatField(db_column='InvTotTax', blank=True, null=True)  # Field name made lowercase.
    invtotincl = models.FloatField(db_column='InvTotIncl', blank=True, null=True)  # Field name made lowercase.
    orddiscamnt = models.FloatField(db_column='OrdDiscAmnt', blank=True, null=True)  # Field name made lowercase.
    orddiscamntex = models.FloatField(db_column='OrdDiscAmntEx', blank=True, null=True)  # Field name made lowercase.
    ordtotexcldex = models.FloatField(db_column='OrdTotExclDEx', blank=True, null=True)  # Field name made lowercase.
    ordtottaxdex = models.FloatField(db_column='OrdTotTaxDEx', blank=True, null=True)  # Field name made lowercase.
    ordtotincldex = models.FloatField(db_column='OrdTotInclDEx', blank=True, null=True)  # Field name made lowercase.
    ordtotexcl = models.FloatField(db_column='OrdTotExcl', blank=True, null=True)  # Field name made lowercase.
    ordtottax = models.FloatField(db_column='OrdTotTax', blank=True, null=True)  # Field name made lowercase.
    ordtotincl = models.FloatField(db_column='OrdTotIncl', blank=True, null=True)  # Field name made lowercase.
    busefixedprices = models.BooleanField(db_column='bUseFixedPrices')  # Field name made lowercase.
    idocprinted = models.IntegerField(db_column='iDocPrinted', blank=True, null=True)  # Field name made lowercase.
    iinvnumagentid = models.IntegerField(db_column='iINVNUMAgentID', blank=True, null=True)  # Field name made lowercase.
    fexchangerate = models.FloatField(db_column='fExchangeRate', blank=True, null=True)  # Field name made lowercase.
    fgrvsplitfixedamntforeign = models.FloatField(db_column='fGrvSplitFixedAmntForeign', blank=True, null=True)  # Field name made lowercase.
    finvdiscamntforeign = models.FloatField(db_column='fInvDiscAmntForeign', blank=True, null=True)  # Field name made lowercase.
    finvdiscamntexforeign = models.FloatField(db_column='fInvDiscAmntExForeign', blank=True, null=True)  # Field name made lowercase.
    finvtotexcldexforeign = models.FloatField(db_column='fInvTotExclDExForeign', blank=True, null=True)  # Field name made lowercase.
    finvtottaxdexforeign = models.FloatField(db_column='fInvTotTaxDExForeign', blank=True, null=True)  # Field name made lowercase.
    finvtotincldexforeign = models.FloatField(db_column='fInvTotInclDExForeign', blank=True, null=True)  # Field name made lowercase.
    finvtotexclforeign = models.FloatField(db_column='fInvTotExclForeign', blank=True, null=True)  # Field name made lowercase.
    finvtottaxforeign = models.FloatField(db_column='fInvTotTaxForeign', blank=True, null=True)  # Field name made lowercase.
    finvtotinclforeign = models.FloatField(db_column='fInvTotInclForeign', blank=True, null=True)  # Field name made lowercase.
    forddiscamntforeign = models.FloatField(db_column='fOrdDiscAmntForeign', blank=True, null=True)  # Field name made lowercase.
    forddiscamntexforeign = models.FloatField(db_column='fOrdDiscAmntExForeign', blank=True, null=True)  # Field name made lowercase.
    fordtotexcldexforeign = models.FloatField(db_column='fOrdTotExclDExForeign', blank=True, null=True)  # Field name made lowercase.
    fordtottaxdexforeign = models.FloatField(db_column='fOrdTotTaxDExForeign', blank=True, null=True)  # Field name made lowercase.
    fordtotincldexforeign = models.FloatField(db_column='fOrdTotInclDExForeign', blank=True, null=True)  # Field name made lowercase.
    fordtotexclforeign = models.FloatField(db_column='fOrdTotExclForeign', blank=True, null=True)  # Field name made lowercase.
    fordtottaxforeign = models.FloatField(db_column='fOrdTotTaxForeign', blank=True, null=True)  # Field name made lowercase.
    fordtotinclforeign = models.FloatField(db_column='fOrdTotInclForeign', blank=True, null=True)  # Field name made lowercase.
    ctaxnumber = models.CharField(db_column='cTaxNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    caccountname = models.CharField(db_column='cAccountName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    iprospectid = models.IntegerField(db_column='iProspectID')  # Field name made lowercase.
    iopportunityid = models.IntegerField(db_column='iOpportunityID')  # Field name made lowercase.
    invtotrounding = models.FloatField(db_column='InvTotRounding')  # Field name made lowercase.
    ordtotrounding = models.FloatField(db_column='OrdTotRounding')  # Field name made lowercase.
    finvtotforeignrounding = models.FloatField(db_column='fInvTotForeignRounding')  # Field name made lowercase.
    fordtotforeignrounding = models.FloatField(db_column='fOrdTotForeignRounding')  # Field name made lowercase.
    binvrounding = models.BooleanField(db_column='bInvRounding')  # Field name made lowercase.
    iinvsettlementtermsid = models.IntegerField(db_column='iInvSettlementTermsID')  # Field name made lowercase.
    csettlementterminvmsg = models.CharField(db_column='cSettlementTermInvMsg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    iordercancelreasonid = models.IntegerField(db_column='iOrderCancelReasonID')  # Field name made lowercase.
    ilinkeddocid = models.BigIntegerField(db_column='iLinkedDocID')  # Field name made lowercase.
    blinkedtemplate = models.BooleanField(db_column='bLinkedTemplate')  # Field name made lowercase.
    invtotinclexrounding = models.FloatField(db_column='InvTotInclExRounding')  # Field name made lowercase.
    ordtotinclexrounding = models.FloatField(db_column='OrdTotInclExRounding')  # Field name made lowercase.
    finvtotinclforeignexrounding = models.FloatField(db_column='fInvTotInclForeignExRounding')  # Field name made lowercase.
    fordtotinclforeignexrounding = models.FloatField(db_column='fOrdTotInclForeignExRounding')  # Field name made lowercase.
    ieunotcid = models.IntegerField(db_column='iEUNoTCID')  # Field name made lowercase.
    ipoauthstatus = models.IntegerField(db_column='iPOAuthStatus')  # Field name made lowercase.
    ipoincidentid = models.IntegerField(db_column='iPOIncidentID')  # Field name made lowercase.
    isupervisorid = models.IntegerField(db_column='iSupervisorID', blank=True, null=True)  # Field name made lowercase.
    imergeddocid = models.BigIntegerField(db_column='iMergedDocID')  # Field name made lowercase.
    idocemailed = models.IntegerField(db_column='iDocEmailed')  # Field name made lowercase.
    fdepositamountforeign = models.FloatField(db_column='fDepositAmountForeign', blank=True, null=True)  # Field name made lowercase.
    frefundamount = models.FloatField(db_column='fRefundAmount', blank=True, null=True)  # Field name made lowercase.
    btaxperline = models.BooleanField(db_column='bTaxPerLine')  # Field name made lowercase.
    fdepositamounttotal = models.FloatField(db_column='fDepositAmountTotal', blank=True, null=True)  # Field name made lowercase.
    fdepositamountunallocated = models.FloatField(db_column='fDepositAmountUnallocated', blank=True, null=True)  # Field name made lowercase.
    fdepositamountnew = models.FloatField(db_column='fDepositAmountNew', blank=True, null=True)  # Field name made lowercase.
    fdepositamounttotalforeign = models.FloatField(db_column='fDepositAmountTotalForeign', blank=True, null=True)  # Field name made lowercase.
    fdepositamountunallocatedforeign = models.FloatField(db_column='fDepositAmountUnallocatedForeign', blank=True, null=True)  # Field name made lowercase.
    frefundamountforeign = models.FloatField(db_column='fRefundAmountForeign', blank=True, null=True)  # Field name made lowercase.
    keepasidecollectiondate = models.DateTimeField(db_column='KeepAsideCollectionDate', blank=True, null=True)  # Field name made lowercase.
    keepasideexpirydate = models.DateTimeField(db_column='KeepAsideExpiryDate', blank=True, null=True)  # Field name made lowercase.
    ccontact = models.CharField(db_column='cContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ctelephone = models.CharField(db_column='cTelephone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cfax = models.CharField(db_column='cFax', max_length=25, blank=True, null=True)  # Field name made lowercase.
    cemail = models.CharField(db_column='cEmail', max_length=60, blank=True, null=True)  # Field name made lowercase.
    ccellular = models.CharField(db_column='cCellular', max_length=25, blank=True, null=True)  # Field name made lowercase.
    imgordersignature = models.BinaryField(db_column='imgOrderSignature', blank=True, null=True)  # Field name made lowercase.
    iinsurancestate = models.IntegerField(db_column='iInsuranceState')  # Field name made lowercase.
    cauthorisedby = models.CharField(db_column='cAuthorisedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cclaimnumber = models.CharField(db_column='cClaimNumber', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cpolicynumber = models.CharField(db_column='cPolicyNumber', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dincidentdate = models.DateTimeField(db_column='dIncidentDate', blank=True, null=True)  # Field name made lowercase.
    cexcessaccname = models.CharField(db_column='cExcessAccName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    cexcessacccont1 = models.CharField(db_column='cExcessAccCont1', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cexcessacccont2 = models.CharField(db_column='cExcessAccCont2', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fexcessamt = models.FloatField(db_column='fExcessAmt', blank=True, null=True)  # Field name made lowercase.
    fexcesspct = models.FloatField(db_column='fExcessPct', blank=True, null=True)  # Field name made lowercase.
    fexcessexclusive = models.FloatField(db_column='fExcessExclusive')  # Field name made lowercase.
    fexcessinclusive = models.FloatField(db_column='fExcessInclusive')  # Field name made lowercase.
    fexcesstax = models.FloatField(db_column='fExcessTax')  # Field name made lowercase.
    faddchargeexclusive = models.FloatField(db_column='fAddChargeExclusive')  # Field name made lowercase.
    faddchargetax = models.FloatField(db_column='fAddChargeTax')  # Field name made lowercase.
    faddchargeinclusive = models.FloatField(db_column='fAddChargeInclusive')  # Field name made lowercase.
    faddchargeexclusiveforeign = models.FloatField(db_column='fAddChargeExclusiveForeign')  # Field name made lowercase.
    faddchargetaxforeign = models.FloatField(db_column='fAddChargeTaxForeign')  # Field name made lowercase.
    faddchargeinclusiveforeign = models.FloatField(db_column='fAddChargeInclusiveForeign')  # Field name made lowercase.
    fordaddchargeexclusive = models.FloatField(db_column='fOrdAddChargeExclusive')  # Field name made lowercase.
    fordaddchargetax = models.FloatField(db_column='fOrdAddChargeTax')  # Field name made lowercase.
    fordaddchargeinclusive = models.FloatField(db_column='fOrdAddChargeInclusive')  # Field name made lowercase.
    fordaddchargeexclusiveforeign = models.FloatField(db_column='fOrdAddChargeExclusiveForeign')  # Field name made lowercase.
    fordaddchargetaxforeign = models.FloatField(db_column='fOrdAddChargeTaxForeign')  # Field name made lowercase.
    fordaddchargeinclusiveforeign = models.FloatField(db_column='fOrdAddChargeInclusiveForeign')  # Field name made lowercase.
    iinvoicesplitdocid = models.BigIntegerField(db_column='iInvoiceSplitDocID')  # Field name made lowercase.
    cgivnumber = models.CharField(db_column='cGIVNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bisdcorder = models.BooleanField(db_column='bIsDCOrder')  # Field name made lowercase.
    idcbranchid = models.IntegerField(db_column='iDCBranchID', blank=True, null=True)  # Field name made lowercase.
    isalesbranchid = models.IntegerField(db_column='iSalesBranchID', blank=True, null=True)  # Field name made lowercase.
    invnum_ibranchid = models.IntegerField(db_column='InvNum_iBranchID', blank=True, null=True)  # Field name made lowercase.
    invnum_dcreateddate = models.DateTimeField(db_column='InvNum_dCreatedDate', blank=True, null=True)  # Field name made lowercase.
    invnum_dmodifieddate = models.DateTimeField(db_column='InvNum_dModifiedDate', blank=True, null=True)  # Field name made lowercase.
    invnum_icreatedbranchid = models.IntegerField(db_column='InvNum_iCreatedBranchID', blank=True, null=True)  # Field name made lowercase.
    invnum_imodifiedbranchid = models.IntegerField(db_column='InvNum_iModifiedBranchID', blank=True, null=True)  # Field name made lowercase.
    invnum_icreatedagentid = models.IntegerField(db_column='InvNum_iCreatedAgentID', blank=True, null=True)  # Field name made lowercase.
    invnum_imodifiedagentid = models.IntegerField(db_column='InvNum_iModifiedAgentID', blank=True, null=True)  # Field name made lowercase.
    invnum_ichangesetid = models.IntegerField(db_column='InvNum_iChangeSetID', blank=True, null=True)  # Field name made lowercase.
    invnum_checksum = models.TextField(db_column='InvNum_Checksum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    icancellationreasonid = models.IntegerField(db_column='iCancellationReasonID', blank=True, null=True)  # Field name made lowercase.
    bidfproccessed = models.BooleanField(db_column='bIDFProccessed')  # Field name made lowercase.
    bsbsi = models.BooleanField(db_column='bSBSI')  # Field name made lowercase.
    iimportdeclarationid = models.IntegerField(db_column='iImportDeclarationID', blank=True, null=True)  # Field name made lowercase.
    cpermitnumber = models.CharField(db_column='cPermitNumber', max_length=20)  # Field name made lowercase.
    breversechargeapplied = models.BooleanField(db_column='bReverseChargeApplied')  # Field name made lowercase.
    breversechargecustoms = models.BooleanField(db_column='bReverseChargeCustoms')  # Field name made lowercase.
    creversechargeauditnr = models.CharField(db_column='cReverseChargeAuditNr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    istateid = models.IntegerField(db_column='iStateID', blank=True, null=True)  # Field name made lowercase.
    cdpordservicetaskno = models.CharField(db_column='cDPOrdServiceTaskNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdsordservicetaskno = models.CharField(db_column='cDSOrdServiceTaskNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdcrnservicetaskno = models.CharField(db_column='cDCrnServiceTaskNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cdsmextordernum = models.CharField(db_column='cDSMExtOrderNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    flatitude = models.FloatField(db_column='fLatitude', blank=True, null=True)  # Field name made lowercase.
    flongitude = models.FloatField(db_column='fLongitude', blank=True, null=True)  # Field name made lowercase.
    chash = models.CharField(db_column='cHash', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'InvNum'