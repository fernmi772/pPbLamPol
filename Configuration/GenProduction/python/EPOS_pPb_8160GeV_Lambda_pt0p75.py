import FWCore.ParameterSet.Config as cms

generator = cms.EDFilter("ReggeGribovPartonMCGeneratorFilter",

			 bmin = cms.double(0), #impact parameter min in fm
			 bmax = cms.double(10000),#impact parameter max in fm
			 paramFileName = cms.untracked.string("Configuration/Generator/data/ReggeGribovPartonMC.param"), #file with more parameters specific to crmc interface
			 skipNuclFrag = cms.bool(True), #in HI collisions nuclear fragments with pt=0 can be in the hep event. to skip those activate this option
			 beammomentum = cms.double(4080),
			 targetmomentum = cms.double(-4080),
			 beamid = cms.int32(1),
			 targetid = cms.int32(208),
			 model = cms.int32(0),
			 )


configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.2 $'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/CMSSW/Configuration/Generator/python/ReggeGribovPartonMC_EposLHC_4080_4080GeV_pPb_cfi.py,v $'),
    annotation = cms.untracked.string('ReggeGribovMC generator')
    )

particlefilter = cms.EDFilter("MCSingleParticleFilter",
    MaxEta = cms.untracked.vdouble(2.5,2.5),
    Status = cms.untracked.vint32(1,1),
    MinEta = cms.untracked.vdouble(-2.5,-2.5),
    MinPt = cms.untracked.vdouble(0.75,0.75),
    ParticleID = cms.untracked.vint32(3122,-3122)
)

ProductionFilterSequence = cms.Sequence(generator+particlefilter)

