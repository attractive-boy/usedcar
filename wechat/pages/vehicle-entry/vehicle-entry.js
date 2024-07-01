Page({
  data: {
    form: {
      photo: [],
      model: '',
      year: '',
      mileage: '',
      licensePlate: '',
      accountNumber: '',
      color: '',
      insuranceCompulsory: false,
      insuranceCompulsoryEndDate: '',
      insuranceThirdParty: false,
      insuranceThirdPartyEndDate: '',
      previousOwnerName: '',
      previousOwnerWeChat: '',
      previousOwnerPhone: '',
      vehicleFrameNumber: '',
      purchaseAmount: '',
      purchaser: '',
      additionalFee: false,
      additionalFeeDetail: '',
      additionalFeeAmount: '',
      purchaserPickerVisible:false,
    },
    accountNumbers: [
      { label: '1', value: '1' },
      { label: '2', value: '2' },
      { label: '3', value: '3' },
      { label: '4', value: '4' },
      { label: '5', value: '5' },
      { label: '6', value: '6' },
      { label: '7', value: '7' },
      { label: '8', value: '8' },
      { label: '9', value: '9' },
    ],
    staffList: [],
    purchaserName: '',
    fileList: [],
  },
  onLoad(){
    this.getUsers();
  },
  getUsers(){
    const that = this;
    getApp().request('/user','GET').then(res => {
      let data = res.data;
      data = data.map(item => {
        item.label = `${item.name} - ${item.phone}`;
        item.value = item.id;
        return item;
      })
      that.setData({ staffList: data });
    })
  },

  onInputChange(e) {
    const field = e.currentTarget.dataset.field;
    console.log(field,e.detail.value)
    this.setData({ [`form.${field}`]: e.detail.value });
  },

  onYearChange(e) {
    this.setData({ 'form.year': e.detail.value });
  },

  onAccountNumberChange(e) {
    this.setData({ 'form.accountNumber': e.detail.value });
  },

  onInsuranceCompulsoryChange(e) {
    this.setData({ 'form.insuranceCompulsory': e.detail.value });
    if (!e.detail.value) {
      this.setData({ 'form.insuranceCompulsoryEndDate': '' });
    }
  },

  onInsuranceCompulsoryEndDateChange(e) {
    this.setData({ 'form.insuranceCompulsoryEndDate': e.detail.value });
  },

  onInsuranceThirdPartyChange(e) {
    this.setData({ 'form.insuranceThirdParty': e.detail.value });
    if (!e.detail.value) {
      this.setData({ 'form.insuranceThirdPartyEndDate': '' });
    }
  },

  onInsuranceThirdPartyEndDateChange(e) {
    this.setData({ 'form.insuranceThirdPartyEndDate': e.detail.value });
  },

  onPurchaserChange(e) {
    this.setData({ 
      'form.purchaser':  e.detail.value,
      purchaserName: this.data.staffList.find(item => item.id == e.detail.value).name
    });
  },
  showPurchaserPicker(){
    this.setData({ purchaserPickerVisible: true });
  },

  onAdditionalFeeChange(e) {
    this.setData({ 'form.additionalFee': e.detail.value });
    if (!e.detail.value) {
      this.setData({
        'form.additionalFeeDetail': '',
        'form.additionalFeeAmount': ''
      });
    }
  },
  showAccountNumberPicker(){
      this.setData({ accountNumberPickerVisible: true });
  },
  onEndDateChange(e){
    this.setData({ 'form.insuranceCompulsoryEndDate': e.detail.value });
  },
  onSubmit() {
    console.log('Form data:', this.data.form);
    getApp().request('/vehicle', 'POST', this.data.form).then(res => {
      if(res.status == 201){
        wx.showToast({
          title: '提交成功',
          icon: 'success',
          duration: 2000
        });
      }
      else{
        wx.showToast({
          title: '提交失败',
          icon: 'error',
          duration: 2000
        });
      }
    });
  },
  handleAdd(e) {
    const { files } = e.detail;

    files.forEach(file => this.uploadFile(file))
  },
  uploadFile(file) {
    const { fileList } = this.data;

    this.setData({
      fileList: [...fileList, { ...file, status: 'loading' }],
    });
    const { length } = fileList;
    const { baseUrl } = require('../../config/index');
    const task = wx.uploadFile({
      url: `${baseUrl}/vehicle/upload`,
      filePath: file.url,
      name: 'file',
      formData: { user: 'test' },
      success: (res) => {
        console.log(res);
        this.setData({
          [`fileList[${length}].status`]: 'done',
          'form.photo': baseUrl + '/vehicle/download/' + JSON.parse(res.data).filename
        });
      },
    });
    task.onProgressUpdate((res) => {
      this.setData({
        [`fileList[${length}].percent`]: res.progress,
      });
    });
  },
  handleRemove(e) {
    const { index } = e.detail;
    const { fileList } = this.data;

    fileList.splice(index, 1);
    this.setData({
      fileList,
    });
  },
});
