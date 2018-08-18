function translateRouteStatusType (routeStatusType) {
  const translations = {
    'o': 'On Time',
    'a': 'Arrived',
    'd': 'Delayed',
  }
  if (routeStatusType in translations) {
    return translations[routeStatusType];
  }
  return '';
}

module.exports = {
  translateRouteStatusType: translateRouteStatusType,
};
