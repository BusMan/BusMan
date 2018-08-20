const viewModesEnum = Object.freeze({
  'EMPTY': 1,
  'BLANK_SPACE': 2,
  'FILLED_SPACE': 3
});

const actionsEnum = Object.freeze({
  'ASSIGN_BUS': 'assign',
  'DELAY_BUS': 'delay',
  'UNASSIGN_BUS': 'unassign',
  'SEARCH': 'search'
})

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
  translateRouteStatusType,
  viewModesEnum,
  actionsEnum
};
